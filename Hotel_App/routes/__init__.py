from .auth_routes import auth_bp
from .cliente_routes import cliente_bp
from .habitacion_routes import habitacion_bp
from .reserva_routes import reserva_bp

def init_app(app):
    # Registra el blueprint para las rutas de autenticación (login, registro, logout)
    app.register_blueprint(auth_bp)

    # Registra el blueprint para las rutas relacionadas con los clientes,
    # con un prefijo de URL "/clientes"
    app.register_blueprint(cliente_bp, url_prefix='/clientes')

    # Registra el blueprint para las rutas relacionadas con las habitaciones,
    # con un prefijo de URL "/habitaciones"
    app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')

    # Registra el blueprint para las rutas relacionadas con las reservas,
    # con un prefijo de URL "/reservas"
    app.register_blueprint(reserva_bp, url_prefix='/reservas')

