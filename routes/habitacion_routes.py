from flask import Blueprint, jsonify, request, flash
from models import db  # Asegúrate de que el modelo y la conexión a la base de datos estén correctamente configurados

habitacion_bp = Blueprint('habitaciones', __name__)

# Ruta para obtener todas las habitaciones
@habitacion_bp.route('/', methods=['GET'])
def get_habitaciones():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM habitaciones")
    rows = cursor.fetchall()
    
    habitaciones = []
    for row in rows:
        habitacion = {
            'id': row[0],
            'numero_habitacion': row[1],
            'tipo': row[2],
            'descripcion': row[3],
            'precio': float(row[4]),  # Asegúrate de convertir el precio a flotante
            'estado': row[5],
            'imagen': row[6]  # Puede ser una URL o una ruta de la imagen, dependiendo de tu estructura
        }
        habitaciones.append(habitacion)
    
    return jsonify(habitaciones)  # Devolver la lista de habitaciones como respuesta JSON

# Ruta para obtener una habitación por ID
@habitacion_bp.route('/<int:id>', methods=['GET'])
def get_habitacion(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM habitaciones WHERE id = %s", (id,))
    row = cursor.fetchone()
    
    if row:
        habitacion = {
            'id': row[0],
            'numero_habitacion': row[1],
            'tipo': row[2],
            'descripcion': row[3],
            'precio': float(row[4]),
            'estado': row[5],
            'imagen': row[6]
        }
        return jsonify(habitacion)  # Devolver la habitación como respuesta JSON
    else:
        return jsonify({'message': 'Habitación no encontrada'}), 404  # Si no se encuentra la habitación

# Ruta para crear una nueva habitación
@habitacion_bp.route('/', methods=['POST'])
def create_habitacion():
    data = request.get_json()  # Obtener los datos en formato JSON
    numero_habitacion = data.get('numero_habitacion')
    tipo = data.get('tipo')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    estado = data.get('estado')
    imagen = data.get('imagen')

    # Validar que los datos sean correctos
    if not numero_habitacion or not tipo or not descripcion or not precio or not estado or not imagen:
        return jsonify({'message': 'Faltan datos'}), 400  # Validación de los datos

    cursor = db.connection.cursor()
    cursor.execute("""
        INSERT INTO habitaciones (numero_habitacion, tipo, descripcion, precio, estado, imagen)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (numero_habitacion, tipo, descripcion, precio, estado, imagen))
    db.connection.commit()  # Guardar los cambios en la base de datos

    return jsonify({'message': 'Habitación creada exitosamente'}), 201  # Responder con éxito

# Ruta para actualizar una habitación existente
@habitacion_bp.route('/<int:id>', methods=['PUT'])
def update_habitacion(id):
    data = request.get_json()  # Obtener los datos en formato JSON
    numero_habitacion = data.get('numero_habitacion')
    tipo = data.get('tipo')
    descripcion = data.get('descripcion')
    precio = data.get('precio')
    estado = data.get('estado')
    imagen = data.get('imagen')

    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM habitaciones WHERE id = %s", (id,))
    row = cursor.fetchone()

    if not row:
        return jsonify({'message': 'Habitación no encontrada'}), 404  # Si no se encuentra la habitación

    # Si la habitación existe, se actualiza
    cursor.execute("""
        UPDATE habitaciones
        SET numero_habitacion = %s, tipo = %s, descripcion = %s, precio = %s, estado = %s, imagen = %s
        WHERE id = %s
    """, (numero_habitacion, tipo, descripcion, precio, estado, imagen, id))
    db.connection.commit()  # Guardar los cambios en la base de datos

    return jsonify({'message': 'Habitación actualizada exitosamente'}), 200  # Responder con éxito

# Ruta para eliminar una habitación
@habitacion_bp.route('/<int:id>', methods=['DELETE'])
def delete_habitacion(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM habitaciones WHERE id = %s", (id,))
    row = cursor.fetchone()

    if not row:
        return jsonify({'message': 'Habitación no encontrada'}), 404  # Si no se encuentra la habitación

    cursor.execute("DELETE FROM habitaciones WHERE id = %s", (id,))
    db.connection.commit()  # Eliminar la habitación de la base de datos

    return jsonify({'message': 'Habitación eliminada exitosamente'}), 200  # Responder con éxito

