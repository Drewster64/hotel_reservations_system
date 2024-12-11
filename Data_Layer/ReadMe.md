Se utilizó mariadb para configurar la base de datos.

Utilizando mysql -u hotel_user -p se accede a la bas de datos con el debido password

Para crear lo necesario:

CREATE DATABASE IF NOT EXISTS hotel_reservations;
USE hotel_reservations;

CREATE TABLE clientes (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
direccion VARCHAR(255),
telefono VARCHAR(20),
email VARCHAR(100) NOT NULL UNIQUE,
fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE habitaciones (
id INT AUTO_INCREMENT PRIMARY KEY,
numero_habitacion VARCHAR(10) NOT NULL UNIQUE,
tipo VARCHAR(50),
descripcion TEXT,
precio DECIMAL(10,2) NOT NULL,
estado VARCHAR(20) DEFAULT 'Disponible',
imagen VARCHAR(255)
);
10

CREATE TABLE reservas (
id INT AUTO_INCREMENT PRIMARY KEY,
cliente_id INT NOT NULL,
habitacion_id INT NOT NULL,
fecha_inicio DATE NOT NULL,
fecha_fin DATE NOT NULL,
estado VARCHAR(20) DEFAULT 'Activa',
fecha_reserva DATETIME DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (cliente_id) REFERENCES clientes(id),
FOREIGN KEY (habitacion_id) REFERENCES habitaciones(id)

Para agregar datos:

INSERT INTO clientes (nombre, direccion, telefono, email)
VALUES
('Juan Pérez', 'Calle Falsa 123', '555-1234',
'juan.perez@example.com'),
('María García', 'Avenida Siempre Viva 456', '555-5678',
'maria.garcia@example.com'),
('Carlos López', 'Boulevard de los Sueños 789', '555-9012',
'carlos.lopez@example.com');
INSERT INTO habitaciones (numero_habitacion, tipo, descripcion,
precio, estado, imagen)
VALUES
('101', 'Sencilla', 'Habitación sencilla con cama individual',
50.00, 'Disponible', '/imagenes_habitaciones/101.jpg'),
('102', 'Doble', 'Habitación doble con dos camas individuales',
75.00, 'Disponible', '/imagenes_habitaciones/102.jpg'),
('201', 'Matrimonial', 'Habitación matrimonial con cama king
size', 100.00, 'Disponible', '/imagenes_habitaciones/201.jpg'),
('202', 'Suite', 'Suite de lujo con vista al mar', 150.00,
'Disponible', '/imagenes_habitaciones/202.jpg'),
11
('301', 'Presidencial', 'Habitación presidencial con todas las
comodidades', 250.00, 'Disponible',
'/imagenes_habitaciones/301.jpg');
INSERT INTO reservas (cliente_id, habitacion_id, fecha_inicio,
fecha_fin, estado)
VALUES
(1, 101, '2023-01-15', '2023-01-20', 'Activa'),
(2, 201, '2023-02-01', '2023-02-05', 'Activa'),
(3, 202, '2023-03-10', '2023-03-15', 'Activa');