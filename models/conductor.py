from conexionBD import Conexion as db
import json

class Conductor:
    def __init__(self, id_conductor=None, tipoDoc=None, numeroDoc=None, apellidos=None, nombres=None, direccion=None, fechaNac=None, estado=None, USUARIOid=None):
        self.id_conductor = id_conductor
        self.tipoDoc = tipoDoc
        self.numeroDoc = numeroDoc
        self.apellidos = apellidos
        self.nombres = nombres
        self.direccion = direccion
        self.fechaNac = fechaNac
        self.estado = estado
        self.USUARIOid = USUARIOid

    def listadoConductores(self):
        con = db().open

        cursor = con.cursor()

        sql = """
            SELECT * 
            FROM CONDUCTOR
            """
        
        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de los conductores'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})

    def registrarConductor(self):
        con=db().open 
        con.autocommit=False
        cursor=con.cursor()
        sql="""insert into conductor (tipoDoc, numeroDoc, apellidos, nombres, direccion, fechaNac, estado, USUARIOid) 
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            cursor.execute(sql,[self.tipoDoc,self.numeroDoc,self.apellidos,self.nombres,self.direccion,self.fechaNac,self.estado,self.USUARIOid])
            con.commit()
            return json.dumps({'status':True,'data':None,'message':'Conductor registrado correctamente'})
        except con.Error as error:
            con.rollback()
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()