from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import db
from models.usuario import Usuario  

auth_bp = Blueprint('auth', __name__)

# Ruta para el login
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')  # Captura el parámetro 'next' para redirigir después
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Buscar al usuario en la base de datos utilizando SQLAlchemy
        user = Usuario.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):  # Verificar que la contraseña sea correcta
            login_user(user)  # Iniciar sesión del usuario
            return redirect(next_page or url_for('home'))  # Redirigir a la página principal (o la página original)
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
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)  # Crear el hash de la contraseña
        nombre = request.form['nombre']
        rol = request.form['rol']  # Agregar el rol si es necesario

        # Verificar si el correo ya está registrado
        user = Usuario.query.filter_by(email=email).first()
        if user:
            flash('El correo ya está registrado')
            return render_template('register.html')  # Volver a mostrar el formulario de registro

        # Crear el nuevo usuario
        new_user = Usuario(email=email, password=password_hash, nombre=nombre, rol=rol)
        db.session.add(new_user)
        db.session.commit()

        flash('Registro exitoso. Inicia sesión para continuar.')
        return redirect(url_for('auth.login'))  # Redirigir al login

    return render_template('register.html')  # Mostrar formulario de registro si es GET

# Decorador para proteger rutas con autenticación
from flask_login import login_required

@auth_bp.route('/clientes', methods=['GET'])
@login_required
def get_clientes():
    # Aquí va la lógica para obtener los clientes de la base de datos
    pass
