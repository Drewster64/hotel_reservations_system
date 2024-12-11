class Reserva:
    def __init__(self, id, cliente_id, habitacion_id, fecha_inicio, fecha_fin, total):
        self.id = id  # Identificador único de la reserva
        self.cliente_id = cliente_id  # ID del cliente que realizó la reserva
        self.habitacion_id = habitacion_id  # ID de la habitación reservada
        self.fecha_inicio = fecha_inicio  # Fecha de inicio de la reserva
        self.fecha_fin = fecha_fin  # Fecha de fin de la reserva
        self.total = total  # Costo total de la reserva

