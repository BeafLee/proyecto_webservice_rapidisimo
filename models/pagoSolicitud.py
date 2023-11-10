from conexionBD import Conexion as db
import json

class PagoSolicitud:
    def __init__(self, id_pago=None, nombre_entidad=None, num_operacion=None, fecha_hora_operacion=None, url_voucher=None):
        self.id_pago = id_pago
        self.nombre_entidad = nombre_entidad
        self.num_operacion = num_operacion
        self.fecha_hora_operacion = fecha_hora_operacion
        self.url_voucher = url_voucher
