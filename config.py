class Config:
    SECRET_KEY = 'BrainBlast'
    MYSQL_HOST = '172.16.254.115'  # IP de VM1
    MYSQL_USER = 'hotel_user'
    MYSQL_PASSWORD = 'JimmyNeutron'
    MYSQL_DB = 'hotel_reservations'

    # MySQL URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

    # Optional: Disable track modifications to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False

