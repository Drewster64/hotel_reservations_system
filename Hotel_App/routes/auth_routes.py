# routes/auth_routes.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.cliente import Cliente  # Asegúrate de que el modelo Cliente esté correctamente importado

auth_bp = Blueprint('auth', __name__)

# Ruta para el login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Verificar las credenciales del usuario en la base de datos
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        row = cursor.fetchone()

        if row and check_password_hash(row[2], password):  # Verificar que la contraseña sea correcta
            user = Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
            login_user(user)  # Iniciar sesión del usuario
            return redirect(url_for('home'))  # Redirigir a la página principal
        else:
            flash('Credenciales inválidas')  # Mostrar mensaje de error
            return render_template('login.html')  # Volver a mostrar el formulario de login
    
    return render_template('login.html')  # Si el método es GET, mostrar el formulario de login

# Ruta para el logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Cerrar sesión del usuario
    return redirect(url_for('auth.login'))  # Redirigir al login

# Ruta para el registro
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Manejar el registro de usuarios
    pass

# Decorador para proteger rutas con autenticación
from flask_login import login_required

@auth_bp.route('/clientes', methods=['GET'])
@login_required
def get_clientes():
    # Solo usuarios autenticados pueden acceder
    pass

