from conexionBD import Conexion as db
import json

class SolicitudServicio:
    def __init__(self, id_solicitud=None, descripcion_carga=None, clase_carga=None, tipo_carga=None, categoria_carga=None, peso_kg=None, fecha_hora_partida=None, fecha_hora_llegada=None, direccion_origen=None, direccion_destino=None, monto_pagar=None, distancia_km=None, tarifa_id=None, pago_solicitud_id=None, estado_solicitud_id=None, cliente_id=None):
        self.id_solicitud = id_solicitud
        self.descripcion_carga = descripcion_carga
        self.clase_carga = clase_carga
        self.tipo_carga = tipo_carga
        self.categoria_carga = categoria_carga
        self.peso_kg = peso_kg
        self.fecha_hora_partida = fecha_hora_partida
        self.fecha_hora_llegada = fecha_hora_llegada
        self.direccion_origen = direccion_origen
        self.direccion_destino = direccion_destino
        self.monto_pagar = monto_pagar
        self.distancia_km = distancia_km
        self.tarifa_id = tarifa_id
        self.pago_solicitud_id = pago_solicitud_id
        self.cliente_id = cliente_id
