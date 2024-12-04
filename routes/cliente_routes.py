from flask import Blueprint, jsonify, request, flash
from flask_login import login_required
from models import db
from models.cliente import Cliente  # Asegúrate de que el modelo Cliente esté correctamente importado

cliente_bp = Blueprint('clientes', __name__)  # Crea un blueprint para gestionar las rutas de clientes

# Ruta para obtener todos los clientes
@cliente_bp.route('/', methods=['GET'])
@login_required  # Proteger la ruta, solo accesible por usuarios autenticados
def get_clientes():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()  # Obtener todos los clientes desde la base de datos
    return jsonify(clientes), 200  # Retornar los clientes en formato JSON

# Ruta para obtener un cliente por ID
@cliente_bp.route('/<int:id>', methods=['GET'])
@login_required  # Proteger la ruta
def get_cliente(id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()  # Obtener el cliente por ID desde la base de datos
    if cliente:
        return jsonify(cliente), 200  # Retornar el cliente en formato JSON
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404  # Si no se encuentra, retornar mensaje de error

# Ruta para crear un nuevo cliente
@cliente_bp.route('/', methods=['POST'])
@login_required  # Proteger la ruta
def create_cliente():
    data = request.get_json()  # Obtener los datos en formato JSON
    nombre = data.get('nombre')  # Nombre del cliente
    email = data.get('email')  # Email del cliente
    telefono = data.get('telefono')  # Teléfono del cliente

    if not nombre or not email or not telefono:
        return jsonify({'message': 'Faltan datos'}), 400  # Validación de datos obligatorios

    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s)",
                   (nombre, email, telefono))  # Insertar los datos del cliente en la base de datos
    db.connection.commit()  # Confirmar la transacción
    return jsonify({'message': 'Cliente creado exitosamente'}), 201  # Confirmación de creación

# Ruta para actualizar un cliente existente
@cliente_bp.route('/<int:id>', methods=['PUT'])
@login_required  # Proteger la ruta
def update_cliente(id):
    data = request.get_json()  # Obtener los datos del cliente en formato JSON
    nombre = data.get('nombre')
    email = data.get('email')
    telefono = data.get('telefono')

    if not nombre or not email or not telefono:
        return jsonify({'message': 'Faltan datos'}), 400  # Validación de datos obligatorios

    cursor = db.connection.cursor()
    cursor.execute("UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id = %s",
                   (nombre, email, telefono, id))  # Actualizar los datos del cliente en la base de datos
    db.connection.commit()  # Confirmar los cambios
    return jsonify({'message': 'Cliente actualizado exitosamente'}), 200  # Confirmación de actualización

# Ruta para eliminar un cliente
@cliente_bp.route('/<int:id>', methods=['DELETE'])
@login_required  # Proteger la ruta
def delete_cliente(id):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))  # Eliminar el cliente por ID
    db.connection.commit()  # Confirmar los cambios

    if cursor.rowcount > 0:
        return jsonify({'message': 'Cliente eliminado exitosamente'}), 200  # Confirmación de eliminación
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404  # Si no se encuentra el cliente, retornar error

