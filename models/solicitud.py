from conexionBD import Conexion as db
import json
from util import CustomJsonEncoder
class Solicitud():
    def __init__(self,p_id=None,p_descripcionCarga=None,p_claseCarga=None,p_tipoCarga=None,p_categoriaCarga=None,
                 p_pesoKg=None,p_fechaHoraPartida=None,p_fechaHoraLlegada=None,p_direccionOrigen=None,
                 p_direccionDestino=None,p_montoPagar=None,p_distanciaKm=None,p_TARIFAid=None,p_CLIENTEid=None,p_PAGO_SOLICITUDid=None):
        self.id=p_id
        self.descripcionCarga=p_descripcionCarga
        self.claseCarga=p_claseCarga
        self.tipoCarga=p_tipoCarga
        self.categoriaCarga=p_categoriaCarga
        self.pesoKg=p_pesoKg
        self.fechaHoraPartida=p_fechaHoraPartida
        self.fechaHoraLlegada=p_fechaHoraLlegada
        self.direccionOrigen=p_direccionOrigen
        self.direccionDestino=p_direccionDestino
        self.montoPagar=p_montoPagar
        self.distanciaKm=p_distanciaKm
        self.TARIFAid=p_TARIFAid
        self.CLIENTEid=p_CLIENTEid
        self.PAGO_SOLICITUDid=p_PAGO_SOLICITUDid
    
    def listarSolicitud(self,id):
        con = db().open

        #Crear un cursor
        cursor = con.cursor()
        if id == 0:
            sql =   """
                        select 
                            *
                        from 
                            solicitud_servicio 
                        order by 
                            id desc
                    """
            #Ejecutar la sentencia
            cursor.execute(sql)
        else:
            sql =   """
                        select 
                            *
                            from 
                            solicitud_servicio  
                        where 
                            CLIENTEid = %s
                    """
            #Ejecutar la sentencia
            cursor.execute(sql, [id])
        
        #Recuperar los datos y almacenarlos en la variable "datos"
        solicitudes = cursor.fetchall()
        cursor.close()
        con.close()

        #Retornar los resultados
        if solicitudes:
            return json.dumps({'status': True, 'data': solicitudes, 'message': 'Lista de solicitudes'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
