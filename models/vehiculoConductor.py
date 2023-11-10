from conexionBD import Conexion as db
import json

class VehiculoConductor:
    def __init__(self, vehiculo_id=None, conductor_id=None, latitud=None, longitud=None, solicitud_servicio_id=None):
        self.vehiculo_id = vehiculo_id
        self.conductor_id = conductor_id
        self.latitud = latitud
        self.longitud = longitud
        self.solicitud_servicio_id = solicitud_servicio_id
