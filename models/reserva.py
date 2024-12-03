# models/reserva.py
class Reserva:
    def __init__(self, id, cliente_id, habitacion_id, fecha_inicio, fecha_fin, total):
        self.id = id
        self.cliente_id = cliente_id
        self.habitacion_id = habitacion_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total = total

