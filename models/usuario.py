from flask_login import UserMixin  # Importa UserMixin de Flask-Login para añadir funcionalidades relacionadas con la autenticación

class Usuario(UserMixin):
    def __init__(self, id, email, password, nombre, rol):
        self.id = id  # Identificador único del usuario
        self.email = email  # Correo electrónico del usuario
        self.password = password  # Contraseña del usuario
        self.nombre = nombre  # Nombre completo del usuario
        self.rol = rol  # Rol del usuario ('cliente' o 'admin')

