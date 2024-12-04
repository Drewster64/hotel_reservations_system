from flask import Flask, jsonify
from config import Config
from models import db, Usuario  # Asegúrate de que la clase Usuario esté importada desde models
from flask_login import LoginManager
from flask_cors import CORS  # Importa CORS
from routes.auth_routes import auth_bp
from routes.cliente_routes import cliente_bp
from routes.habitacion_routes import habitacion_bp
from routes.reserva_routes import reserva_bp
from flask_sqlalchemy import SQLAlchemy

# Inicializa la aplicación Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar CORS para permitir solicitudes de cualquier origen en las rutas de la API
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configurar la base de datos
db = SQLAlchemy(app)

# Configurar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Método load_user para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    row = cursor.fetchone()
    if row:
        # Asumimos que la clase Usuario está definida y toma los valores del cursor
        return Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
    else:
        return None

# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp, url_prefix='/clientes')
app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
app.register_blueprint(reserva_bp, url_prefix='/reservas')

# Error Handlers

@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'message': 'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

