from conexionBD import Conexion as db
import json
class Tarifa():
    def __init__(self,p_id=None,p_tarifa=None,p_estado=None,p_fechaHoraInicio=None,p_fechaHoraFin=None):
        self.id=p_id
        self.tarifa=p_tarifa
        self.estado=p_estado
        self.fechaHoraInicio=p_fechaHoraInicio
        self.fechaHoraFin=p_fechaHoraFin
    def registrarTarifa(self):
        con = db().open
        cursor = con.cursor()
        #Sentencia para dar de baja la tarifa actual antes de ingresar la tarifa nueva
        sql_darbaja = """UPDATE TARIFA
        SET estado = 'V', fechaHoraFin = CURRENT_TIMESTAMP
        WHERE id = (SELECT max_id FROM (SELECT MAX(id) AS max_id FROM TARIFA) AS t);"""
        cursor.execute(sql_darbaja)
        sql_registrar="""insert into TARIFA(tarifa,estado,fechaHoraInicio) values(%s,'A',CURRENT_TIMESTAMP)
        """
        print(self.tarifa)        
        try:
           cursor.execute(sql_registrar,[self.tarifa])      
           con.commit()
           return json.dumps({'status':True,'data':None,'message':'Tarifa registrada correctamente'})  
        except:
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()
    
        
        