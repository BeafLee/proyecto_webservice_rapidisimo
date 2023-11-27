from conexionBD import Conexion as db
import json
from util import CustomJsonEncoder
class Estado():
    def __init__(self,p_id=None,p_nombreEstado=None,p_fechaHoraRegistro=None,p_observacion=None, p_estado=None, p_solicitud_servicio_id=None):
        self.id=p_id
        self.nombreEstado=p_nombreEstado
        self.fechaHoraRegistro=p_fechaHoraRegistro
        self.observacion=p_observacion
        self.estado = p_estado
        self.solicitud_servicio_id = p_solicitud_servicio_id
    def registrar_estado(self):
        con = db().open
        cursor = con.cursor()
        #Sentencia para dar de baja la tarifa actual antes de ingresar la tarifa nueva
        sql_desactivar="""UPDATE ESTADO_SOLICITUD 
                            SET estado='V' 
                            WHERE id = (
                                SELECT max_id 
                                FROM (
                                    SELECT MAX(id) AS max_id 
                                    FROM estado_solicitud 
                                    WHERE solicitud_servicioid = %s
                                ) AS subquery_alias
                            )
                            """
        cursor.execute(sql_desactivar,[self.solicitud_servicio_id])
        sql_registrar="""insert into ESTADO_SOLICITUD(nombreEstado,fechaHoraRegistro,observacion,estado,SOLICITUD_SERVICIOid) values(%s,CURRENT_TIMESTAMP,%s,'A',%s)
        """        
        try:
           cursor.execute(sql_registrar,[self.nombreEstado,self.observacion,self.solicitud_servicio_id])      
           con.commit()
           return json.dumps({'status':True,'data':None,'message':'Estado registrado correctamente'})  
        except con.Error as error:
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()
    def cambiarEstado(self):
        con = db().open
        cursor = con.cursor()
        #Sentencia para dar de baja la tarifa actual antes de ingresar la tarifa nueva
        sql_darbaja = """UPDATE estado_solicitud
        SET estado = %s WHERE id = %s;"""
        try:
           cursor.execute(sql_darbaja,[self.id])     
           con.commit()
           return json.dumps({'status':True,'data':None,'message':'Estado actualizado correctamente'})  
        except con.Error as error:
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()