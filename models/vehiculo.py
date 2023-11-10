from conexionBD import Conexion as db
import json

class Vehiculo:
    def __init__(self, id_vehiculo=None, matricula=None, capacidad_total=None, tipo_carga=None, modelo=None, marca=None):
        self.id_vehiculo = id_vehiculo
        self.matricula = matricula
        self.capacidad_total = capacidad_total
        self.tipo_carga = tipo_carga
        self.modelo = modelo
        self.marca = marca
