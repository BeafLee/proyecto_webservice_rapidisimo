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

    def listadoVehiculos(self):
        con = db().open

        cursor = con.cursor()

        sql = """
            SELECT * 
            FROM VEHICULO
            """
        
        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de los vehículos'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})

    def registrarVehiculo(self):
        con=db().open 
        con.autocommit=False
        cursor=con.cursor()
        sql="""insert into vehiculo (matricula, capacidadTotal, tipoCarga, modelo, marca) 
                    values(%s,%s,%s,%s,%s)"""
        try:
            cursor.execute(sql,[self.matricula,self.capacidad_total,self.tipo_carga,self.modelo,self.marca])
            con.commit()
            return json.dumps({'status':True,'data':None,'message':'Vehículo registrado correctamente'})
        except con.Error as error:
            con.rollback()
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()