from flask import Blueprint, jsonify, request, flash
from flask_login import login_required
from models import db
from models.cliente import Cliente  # Asegúrate de que el modelo Cliente esté correctamente importado

cliente_bp = Blueprint('clientes', __name__)

# Ruta para obtener todos los clientes
@cliente_bp.route('/', methods=['GET'])
@login_required  # Proteger la ruta, solo accesible por usuarios autenticados
def get_clientes():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    # Convertir los resultados en formato JSON
    return jsonify(clientes), 200

# Ruta para obtener un cliente por ID
@cliente_bp.route('/<int:id>', methods=['GET'])
@login_required  # Proteger la ruta
def get_cliente(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()
    if cliente:
        return jsonify(cliente), 200  # Retornar el cliente en formato JSON
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404

# Ruta para crear un nuevo cliente
@cliente_bp.route('/', methods=['POST'])
@login_required  # Proteger la ruta
def create_cliente():
    # Obtener los datos del cliente desde la solicitud JSON
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    telefono = data.get('telefono')

    if not nombre or not email or not telefono:
        return jsonify({'message': 'Faltan datos'}), 400  # Validar que todos los campos estén presentes

    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
                   (nombre, email, telefono))
    db.connection.commit()  # Guardar los cambios en la base de datos
    return jsonify({'message': 'Cliente creado exitosamente'}), 201  # Confirmar creación exitosa

# Ruta para actualizar un cliente existente
@cliente_bp.route('/<int:id>', methods=['PUT'])
@login_required  # Proteger la ruta
def update_cliente(id):
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    telefono = data.get('telefono')

    if not nombre or not email or not telefono:
        return jsonify({'message': 'Faltan datos'}), 400  # Validar que todos los campos estén presentes

    cursor = db.connection.cursor()
    cursor.execute("UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id = %s",
                   (nombre, email, telefono, id))
    db.connection.commit()  # Guardar los cambios
    return jsonify({'message': 'Cliente actualizado exitosamente'}), 200

# Ruta para eliminar un cliente
@cliente_bp.route('/<int:id>', methods=['DELETE'])
@login_required  # Proteger la ruta
def delete_cliente(id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
    db.connection.commit()  # Guardar los cambios

    if cursor.rowcount > 0:
        return jsonify({'message': 'Cliente eliminado exitosamente'}), 200
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404

