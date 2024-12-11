from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from models import db

# Crear el Blueprint para las rutas de reserva
reserva_bp = Blueprint('reservas', __name__)

# Ruta para obtener todas las reservas
@reserva_bp.route('/', methods=['GET'])
def get_reservas():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM reservas")
    rows = cursor.fetchall()

    reservas = []
    for row in rows:
        reserva = {
            'id': row[0],
            'cliente_id': row[1],
            'habitacion_id': row[2],
            'fecha_inicio': row[3],
            'fecha_fin': row[4]
        }
        reservas.append(reserva)

    return jsonify(reservas)  # Devolver la lista de reservas como respuesta JSON

# Ruta para obtener una reserva por ID
@reserva_bp.route('/<int:id>', methods=['GET'])
def get_reserva(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM reservas WHERE id = %s", (id,))
    row = cursor.fetchone()

    if row:
        reserva = {
            'id': row[0],
            'cliente_id': row[1],
            'habitacion_id': row[2],
            'fecha_inicio': row[3],
            'fecha_fin': row[4]
        }
        return jsonify(reserva)  # Devolver la reserva como respuesta JSON
    else:
        return jsonify({'message': 'Reserva no encontrada'}), 404  # Si no se encuentra la reserva

# Ruta para crear una nueva reserva
@reserva_bp.route('/', methods=['POST'])
@login_required  # Solo usuarios autenticados pueden hacer una reserva
def create_reserva():
    data = request.get_json()  # Obtener los datos en formato JSON
    habitacion_id = data['habitacion_id']
    fecha_inicio = data['fecha_inicio']
    fecha_fin = data['fecha_fin']
    cliente_id = current_user.id  # Obtener el ID del usuario autenticado

    # Validación de datos
    if not habitacion_id or not fecha_inicio or not fecha_fin:
        return jsonify({'message': 'Faltan datos'}), 400  # Validación de los datos

    cursor = db.connection.cursor()
    cursor.execute("""
        INSERT INTO reservas (cliente_id, habitacion_id, fecha_inicio, fecha_fin)
        VALUES (%s, %s, %s, %s)
    """, (cliente_id, habitacion_id, fecha_inicio, fecha_fin))
    db.connection.commit()  # Guardar los cambios en la base de datos

    return jsonify({'message': 'Reserva creada exitosamente'}), 201  # Responder con éxito

# Ruta para actualizar una reserva existente
@reserva_bp.route('/<int:id>', methods=['PUT'])
@login_required  # Solo usuarios autenticados pueden actualizar sus reservas
def update_reserva(id):
    data = request.get_json()  # Obtener los datos en formato JSON
    habitacion_id = data.get('habitacion_id')
    fecha_inicio = data.get('fecha_inicio')
    fecha_fin = data.get('fecha_fin')

    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM reservas WHERE id = %s", (id,))
    row = cursor.fetchone()

    if not row:
        return jsonify({'message': 'Reserva no encontrada'}), 404  # Si no se encuentra la reserva

    # Solo el cliente que hizo la reserva puede actualizarla
    if row[1] != current_user.id:
        return jsonify({'message': 'No autorizado para actualizar esta reserva'}), 403

    # Actualizar los detalles de la reserva
    cursor.execute("""
        UPDATE reservas
        SET habitacion_id = %s, fecha_inicio = %s, fecha_fin = %s
        WHERE id = %s
    """, (habitacion_id, fecha_inicio, fecha_fin, id))
    db.connection.commit()  # Guardar los cambios en la base de datos

    return jsonify({'message': 'Reserva actualizada exitosamente'}), 200  # Responder con éxito

# Ruta para eliminar una reserva
@reserva_bp.route('/<int:id>', methods=['DELETE'])
@login_required  # Solo usuarios autenticados pueden eliminar sus reservas
def delete_reserva(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM reservas WHERE id = %s", (id,))
    row = cursor.fetchone()

    if not row:
        return jsonify({'message': 'Reserva no encontrada'}), 404  # Si no se encuentra la reserva

    # Solo el cliente que hizo la reserva puede eliminarla
    if row[1] != current_user.id:
        return jsonify({'message': 'No autorizado para eliminar esta reserva'}), 403

    cursor.execute("DELETE FROM reservas WHERE id = %s", (id,))
    db.connection.commit()  # Eliminar la reserva de la base de datos

    return jsonify({'message': 'Reserva eliminada exitosamente'}), 200  # Responder con éxito

