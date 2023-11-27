from conexionBD import Conexion as db
import json
from models import cliente
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
                            SOLICITUD_SERVICIO 
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
                            SOLICITUD_SERVICIO  
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
        
    def listarSolicitudAtencion(self, tipo_doc):
        con = db().open
        cursor = con.cursor()

        if tipo_doc=='DNI':
            sql =   """
                    select 
                        S.descripcionCarga,
                        S.claseCarga,
                        S.tipoCarga,
                        S.categoriaCarga,
                        S.pesoKg,
                        S.fechaHoraPartida,
                        S.fechaHoraLlegada,
                        S.direccionOrigen,
                        S.direccionDestino,
                        S.montoPagar,
                        S.distanciaKm,
                        T.tarifa,
                        C.numeroDoc,
                        C.nombres,
                        C.razonSocial,
                        C.direccion,
                        C.email,
                        C.telefono, 
                        concat(P.nombreEntidad, ' - ', P.numOperacion) as pago,
                        VC.nombreEstado
                    from 
                        SOLICITUD_SERVICIO S
                    inner join
                        VEHICULO_CONDUCTOR VC on S.id = VC.SOLICITUD_SERVICIOid
                    inner join
                        CLIENTE C on C.id = S.CLIENTEid
                    inner join
                        PAGO_SOLICITUD P on P.id = S.PAGO_SOLICITUDid
                    inner join
                        TARIFA T on T.id = S.TARIFAid
                    where
                        VC.nombreEstado = 'VEHICULO ASIGNADO'
                        or VC.nombreEstado = 'VEHICULO EN TRANSITO'
                        or VC.nombreEstado = 'VEHICULO DETENIDO'
                        or VC.nombreEstado = 'VEHICULO DETENIDO POR DESCANSO'
                        or VC.nombreEstado = 'VEHÍCULO DETENIDO POR INTERRUPCIÓN'
                    order by 
                        S.id desc
                    """
        elif tipo_doc=='RUC':
            sql =   """
                    select 
                        S.descripcionCarga,
                        S.claseCarga,
                        S.tipoCarga,
                        S.categoriaCarga,
                        S.pesoKg,
                        S.fechaHoraPartida,
                        S.fechaHoraLlegada,
                        S.direccionOrigen,
                        S.direccionDestino,
                        S.montoPagar,
                        S.distanciaKm,
                        T.tarifa,
                        C.numeroDoc,
                        C.razonSocial,
                        C.direccion,
                        C.email,
                        C.telefono, 
                        concat(P.nombreEntidad, ' - ', P.numOperacion) as pago,
                        VC.nombreEstado
                    from 
                        SOLICITUD_SERVICIO S
                    inner join
                        VEHICULO_CONDUCTOR VC on S.id = VC.SOLICITUD_SERVICIOid
                    inner join
                        CLIENTE C on C.id = S.CLIENTEid
                    inner join
                        PAGO_SOLICITUD P on P.id = S.PAGO_SOLICITUDid
                    inner join
                        TARIFA T on T.id = S.TARIFAid
                    where
                        VC.nombreEstado = 'VEHICULO ASIGNADO'
                        or VC.nombreEstado = 'VEHICULO EN TRANSITO'
                        or VC.nombreEstado = 'VEHICULO DETENIDO'
                        or VC.nombreEstado = 'VEHICULO DETENIDO POR DESCANSO'
                        or VC.nombreEstado = 'VEHÍCULO DETENIDO POR INTERRUPCIÓN'
                    order by 
                        S.id desc
                    """
        cursor.execute(sql, [cliente.Cliente.tipo_doc, cliente.Cliente.tipo_doc])

        
        #Recuperar los datos y almacenarlos en la variable "datos"
        solicitudes = cursor.fetchall()
        cursor.close()
        con.close()

        #Retornar los resultados
        if solicitudes:
            return json.dumps({'status': True, 'data': solicitudes, 'message': 'Lista de solicitudes'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
