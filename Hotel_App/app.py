from flask import Flask, jsonify
from config import Config  # Carga la configuración de la app desde config.py
from models import db, Usuario  # Importa la base de datos y el modelo Usuario
from flask_login import LoginManager  # Para manejar la autenticación
from flask_cors import CORS  # Permite solicitudes CORS
from routes.auth_routes import auth_bp  # Blueprint para autenticación
from routes.cliente_routes import cliente_bp  # Blueprint para clientes
from routes.habitacion_routes import habitacion_bp  # Blueprint para habitaciones
from routes.reserva_routes import reserva_bp  # Blueprint para reservas
from flask_sqlalchemy import SQLAlchemy  # Extensión para gestionar base de datos

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)  # Configuración de la app

# Habilita CORS para todas las rutas
CORS(app, resources={r"/*": {"origins": "*"}})  # Esto permite que cualquier origen realice peticiones a tu API

# Configura la base de datos
db = SQLAlchemy(app)

# Configura Flask-Login para la autenticación de usuarios
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Carga un usuario desde la base de datos
@login_manager.user_loader
def load_user(user_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    if row:
        return Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
    return None

# Registra los blueprints para las rutas de la app
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp, url_prefix='/clientes')
app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
app.register_blueprint(reserva_bp, url_prefix='/reservas')

# Manejadores de errores
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'message': 'Error interno del servidor'}), 500

# Ejecuta la aplicación en el puerto 5000
if __name__ == "__main__":
    app.run(host="172.16.5.165", port=5000)
