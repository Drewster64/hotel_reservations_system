# API de Gestión de Reservas

Esta API, desarrollada con Flask, permite gestionar usuarios, clientes, habitaciones y reservas para un sistema de gestión de reservas. La API incluye autenticación, manejo de sesiones y una arquitectura modular utilizando Blueprints.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Máquinas Virtuales y sus IPs](#máquinas-virtuales-y-sus-ips)
- [Configuración](#configuración)
- [Rutas Disponibles](#rutas-disponibles)
- [Manejo de Errores](#manejo-de-errores)
- [Autenticación](#autenticación)

---

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <https://github.com/Drewster64/hotel_reservations_system/tree/main>
   cd <Hotel_reservations_system>
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno en un archivo `config.py`.

4. Inicia la aplicación:
   ```bash
   python app.py
   ```

---

## Máquinas Virtuales y sus IPs

Esta API está distribuida en tres capas, cada una corriendo en una máquina virtual diferente. Las IPs de las máquinas virtuales son las siguientes:

1. **VM1 (Capa de Presentación)**:
   - **Propietario**: Benyahir
   - **IP**: `172.16.5.65`

2. **VM2 (Capa Lógica)**:
   - **Propietario**: Emmanuel
   - **IP**: `172.16.5.255`

3. **VM3 (Capa de Base de Datos)**:
   - **Propietario**: John
   - **IP**: `172.16.254.115`

---
## Configuración

El archivo `config.py` debe incluir las siguientes variables:

```python
class Config:
    SECRET_KEY = 'BrainBlast'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'  # O la URI de tu base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## Rutas Disponibles

La API está organizada en diferentes Blueprints:

### 1. **Autenticación (`auth_routes`)**

- **`POST /login`**: Inicia sesión y devuelve un token JWT.
- **`POST /logout`**: Finaliza la sesión del usuario.
- **`POST /register`**: Registra un nuevo usuario.

### 2. **Clientes (`cliente_routes`)**

- **`GET /clientes`**: Obtiene la lista de clientes.
- **`POST /clientes`**: Crea un nuevo cliente.
- **`GET /clientes/<id>`**: Obtiene los detalles de un cliente por su ID.
- **`PUT /clientes/<id>`**: Actualiza un cliente existente.
- **`DELETE /clientes/<id>`**: Elimina un cliente.

### 3. **Habitaciones (`habitacion_routes`)**

- **`GET /habitaciones`**: Obtiene la lista de habitaciones.
- **`POST /habitaciones`**: Crea una nueva habitación.
- **`GET /habitaciones/<id>`**: Obtiene los detalles de una habitación por su ID.
- **`PUT /habitaciones/<id>`**: Actualiza una habitación existente.
- **`DELETE /habitaciones/<id>`**: Elimina una habitación.

### 4. **Reservas (`reserva_routes`)**

- **`GET /reservas`**: Obtiene la lista de reservas.
- **`POST /reservas`**: Crea una nueva reserva.
- **`GET /reservas/<id>`**: Obtiene los detalles de una reserva por su ID.
- **`PUT /reservas/<id>`**: Actualiza una reserva existente.
- **`DELETE /reservas/<id>`**: Elimina una reserva.

---

## Manejo de Errores

La API maneja errores comunes de la siguiente manera:

- **404 - Recurso no encontrado**: Devuelve un mensaje indicando que el recurso no existe.
- **500 - Error interno del servidor**: Devuelve un mensaje genérico sobre un fallo interno.

Ejemplo de respuesta de error:

```json
{
  "message": "Recurso no encontrado"
}
```

---

## Autenticación

Esta API utiliza **Flask-Login** para manejar sesiones de usuario. Además, soporta la autenticación basada en tokens JWT (si se implementa en `auth_routes`). Asegúrate de incluir el token en el encabezado de las solicitudes autenticadas:

```http
Authorization: Bearer <tu_token_jwt>
```

---

## Ejecución

Ejecuta la aplicación en modo desarrollo:

```bash
python app.py
```

Por defecto, estará disponible en `http://127.0.0.1:5000`.

---

## Notas

1. Asegúrate de inicializar la base de datos ejecutando los scripts correspondientes.
2. Configura correctamente los permisos para endpoints protegidos.
