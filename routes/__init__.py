from .auth_routes import auth_bp
from .cliente_routes import cliente_bp
from .habitacion_routes import habitacion_bp
from .reserva_routes import reserva_bp

def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
    app.register_blueprint(reserva_bp, url_prefix='/reservas')

