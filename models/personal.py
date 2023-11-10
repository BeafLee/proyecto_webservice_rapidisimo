from conexionBD import Conexion as db
import json

class Personal:
    def __init__(self, id_personal=None, tipo_doc=None, numero_doc=None, apellidos=None, nombres=None, direccion=None, email=None, telefono=None, estado=None, fecha_nac=None, usuario_id=None):
        self.id_personal = id_personal
        self.tipo_doc = tipo_doc
        self.numero_doc = numero_doc
        self.apellidos = apellidos
        self.nombres = nombres
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.estado = estado
        self.fecha_nac = fecha_nac
        self.usuario_id = usuario_id
