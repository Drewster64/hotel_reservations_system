class Habitacion:
    def __init__(self, id, numero, tipo, descripcion, precio, disponibilidad):
        self.id = id  # Identificador único de la habitación
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (ej. individual, doble, suite)
        self.descripcion = descripcion  # Descripción adicional de la habitación
        self.precio = precio  # Precio de la habitación por noche
        self.disponibilidad = disponibilidad  # Estado de disponibilidad de la habitación (disponible/no disponible)

