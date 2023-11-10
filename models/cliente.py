from conexionBD import Conexion as db
import json

class Cliente:
    def __init__(self, id_cliente=None, tipo_doc=None, numero_doc=None, nombres=None, razon_social=None, direccion=None, email=None, telefono=None, estado=None, usuario_id=None):
        self.id_cliente = id_cliente
        self.tipo_doc = tipo_doc
        self.numero_doc = numero_doc
        self.nombres = nombres
        self.razon_social = razon_social
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.estado = estado
        self.usuario_id = usuario_id
