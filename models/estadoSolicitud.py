from conexionBD import Conexion as db
import json

class EstadoSolicitud:
    def __init__(self, id_estado=None, nombre_estado=None, fecha_hora_registro=None, observacion=None, estado=None, solicitud_servicio_id=None):
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado
        self.fecha_hora_registro = fecha_hora_registro
        self.observacion = observacion
        self.estado = estado
        self.solicitud_servicio_id = solicitud_servicio_id
