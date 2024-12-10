class Config:
    # Clave secreta utilizada por Flask para sesiones y protección de formularios
    SECRET_KEY = 'BrainBlast'
    
    # Configuración de la base de datos MySQL
    MYSQL_HOST = '172.16.254.115'  # Dirección IP de la máquina que aloja MySQL (VM1)
    MYSQL_USER = 'hotel_user'  # Nombre de usuario para acceder a MySQL
    MYSQL_PASSWORD = 'JimmyNeutron'  # Contraseña del usuario MySQL
    MYSQL_DB = 'hotel_reservations'  # Nombre de la base de datos MySQL

    # URI de conexión a la base de datos MySQL para SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

