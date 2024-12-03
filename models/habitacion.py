# models/habitacion.py
class Habitacion:
    def __init__(self, id, numero, tipo, descripcion, precio, disponibilidad):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio = precio
        self.disponibilidad = disponibilidad

