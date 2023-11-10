from conexionBD import Conexion as db
import json

class EstadoVehiculo:
    def __init__(self, id_estado=None, nombre_estado=None, fecha_hora_registro=None, observacion=None, estado=None, vehiculo_id=None, conductor_id=None):
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado
        self.fecha_hora_registro = fecha_hora_registro
        self.observacion = observacion
        self.estado = estado
        self.vehiculo_id = vehiculo_id
        self.conductor_id = conductor_id
