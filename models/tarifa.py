from conexionBD import Conexion as db
import json

class Tarifa:
    def __init__(self, id_tarifa=None, tarifa=None, estado=None, fecha_hora_inicio=None, fecha_hora_fin=None):
        self.id_tarifa = id_tarifa
        self.tarifa = tarifa
        self.estado = estado
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin
