from conexionBD import Conexion as db
import json

class EstadoSolicitud:
    def __init__(self, id_estado=None, nombre_estado=None, fecha_hora_registro=None, observacion=None, estado=None, solicitud_servicio_id=None):
        self.id_estado = id_estado
        self.nombre_estado = nombre_estado
        self.fecha_hora_registro = fecha_hora_registro
        self.observacion = observacion
        self.estado = estado
        self.solicitud_servicio_id = solicitud_servicio_id


    def listadoEstados(self):
        con = db().open

        cursor = con.cursor()

        sql = """
            SELECT * 
            FROM ESTADO_SOLICITUD 
            WHERE SOLICITUD_SERVICIOid = %s 
            ORDER BY fechaHoraRegistro
            """
        
        cursor.execute(sql, [self.solicitud_servicio_id])

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Historial de estados del servicio'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
