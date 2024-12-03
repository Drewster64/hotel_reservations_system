from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.usuario import Usuario  # Asegúrate de que el modelo Usuario esté correctamente importado

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

        if row and check_password_hash(row[2], password):  # Verificar que la contraseña es correcta
            # Crear una instancia de Usuario y loguear al usuario
            user = Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
            login_user(user)  # Iniciar sesión del usuario
            return redirect(url_for('home'))  # Redirigir a la página principal
        else:
            flash('Credenciales inválidas', 'error')  # Mostrar mensaje de error si las credenciales son incorrectas
            return render_template('login.html')  # Volver a mostrar el formulario de login

    return render_template('login.html')  # Si el método es GET, mostrar el formulario de login

# Ruta para el registro
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        nombre = request.form['nombre']
        rol = request.form['rol']

        # Verificar si el email ya está registrado
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        row = cursor.fetchone()

        if row:
            flash('El email ya está registrado', 'error')  # Mostrar error si el email ya existe
            return render_template('register.html')  # Volver al formulario de registro

        # Encriptar la contraseña antes de almacenarla
        hashed_password = generate_password_hash(password, method='sha256')

        # Insertar el nuevo usuario en la base de datos
        cursor.execute("INSERT INTO usuarios (email, password, nombre, rol) VALUES (%s, %s, %s, %s)",
                       (email, hashed_password, nombre, rol))
        db.connection.commit()  # Confirmar la transacción

        flash('Registro exitoso. Inicia sesión ahora.', 'success')  # Mensaje de éxito
        return redirect(url_for('auth.login'))  # Redirigir al login

    return render_template('register.html')  # Mostrar el formulario de registro si el método es GET

# Ruta para el logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Cerrar sesión del usuario
    return redirect(url_for('auth.login'))  # Redirigir al login

