from conexionBD import Conexion as db
import json
from util import CustomJsonEncoder
class Estado():
    def __init__(self,p_id=None,p_estado=None,p_fechaHoraRegistro=None,p_observacion=None):
        self.id=p_id
        self.estado=p_estado
        self.fechaHoraRegistro=p_fechaHoraRegistro
        self.observacion=p_observacion
    def registrar_estado(self):
        con = db().open
        cursor = con.cursor()
        #Sentencia para dar de baja la tarifa actual antes de ingresar la tarifa nueva
        sql_registrar="""insert into estado_solicitud(estado,fechaHoraRegistro,observacion) values(%s,CURRENT_TIMESTAMP,%s)
        """        
        try:
           cursor.execute(sql_registrar,[self.estado,self.observacion])      
           con.commit()
           return json.dumps({'status':True,'data':None,'message':'Estado registrado correctamente'})  
        except con.Error as error:
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()
        