from conexionBD import Conexion as db
import json

class Conductor:
    def __init__(self, id_conductor=None, tipo_doc=None, numero_doc=None, apellidos=None, nombres=None, direccion=None, fecha_nac=None, estado=None, usuario_id=None):
        self.id_conductor = id_conductor
        self.tipo_doc = tipo_doc
        self.numero_doc = numero_doc
        self.apellidos = apellidos
        self.nombres = nombres
        self.direccion = direccion
        self.fecha_nac = fecha_nac
        self.estado = estado
        self.usuario_id = usuario_id
