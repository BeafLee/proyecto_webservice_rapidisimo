from conexionBD import Conexion as db
import json

class Usuario:
    def __init__(self, id_usuario=None, usuario=None, contrasena=None, tipo_usuario=None, token=None, estado_token=None):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario
        self.token = token
        self.estado_token = estado_token
