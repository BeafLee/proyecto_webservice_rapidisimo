from conexionBD import Conexion as db
import json

class VehiculoConductor:
    def __init__(self, vehiculo_id=None, conductor_id=None, latitud=None, longitud=None, solicitud_servicio_id=None, nombreEstado=None, fechaHoraRegistro=None, observacion=None):
        self.solicitud_servicio_id = solicitud_servicio_id
        self.vehiculo_id = vehiculo_id
        self.conductor_id = conductor_id
        self.latitud = latitud
        self.longitud = longitud
        self.nombreEstado = nombreEstado
        self.fechaHoraRegistro = fechaHoraRegistro
        self.observacion = observacion
        

    def listado(self):
        con = db().open

        cursor = con.cursor()

        sql = ""
        
        if self.solicitud_servicio_id == 0:
            sql = """
            SELECT vc.*, v.matricula, c.apellidos || ', ' || c.nombres as conductor
            FROM VEHICULO_CONDUCTOR vc
                INNER JOIN VEHICULO v on v.id = vc.VEHICULOid
                INNER JOIN CONDUCTOR c on c.id = vc.CONDUCTORid
            WHERE UPPER(nombreEstado) != 'FINALIZADO' 
            """
        else:
            sql = """
            SELECT vc.*, v.matricula, c.apellidos || ', ' || c.nombres as conductor 
            FROM VEHICULO_CONDUCTOR 
            WHERE SOLICITUD_SERVICIOid = %s
            """
        
        cursor.execute(sql, [self.solicitud_servicio_id, self.solicitud_servicio_id])

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Listado de ubicaciones de los vehiculos'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
        
    
    def asignar(self):
        #Abrimos conexion a la bd
        con = db().open
    
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        try:
            #Consulta para registrar 
            sql = "insert into VEHICULO_CONDUCTOR(SOLICITUD_SERVICIOid, VEHICULOid, CONDUCTORid) values (%s,%s,%s)"
            #ejecutar la sentencia sql
            cursor.execute(sql, [self.solicitud_servicio_id, self.vehiculo_id, self.conductor_id])


            #Consulta para actualizar el estado de la solicitud si es que no tiene estado ya
            sql = """
                insert into 
                    ESTADO_SOLICITUD(nombreEstado, fechaHoraRegistro, observacion, estado, SOLICITUD_SERVICIOid) 
                    values ('VEHICULO ASIGNADO', now(), 'Registro automático', 'V', %s) 
                where not exists 
                    (select * from ESTADO_SOLICITUD where SOLICITUD_SERVICIOid = %s)
                """ # * -> 1
            #ejecutar la sentencia sql
            cursor.execute(sql, [self.solicitud_servicio_id, self.solicitud_servicio_id])

            #Confirmar la sentencia de ejecución
            con.commit()

            #retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'La asignación se ha registrado correctamente'})

        except con.Error as error:
            #Revocar la operación
            con.rollback()
            return json.dumps({'status': False, 'data': None, 'message': format(error)})

        finally:
            cursor.close()
            con.close()  


    def actualizarEstado(self):
        #Abrimos conexion a la bd
        con = db().open
    
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        try:
            #Consulta  
            sql = """
                update VEHICULO_CONDUCTOR set 
                    latitud = %s, 
                    longitud = %s, 
                    nombreEstado = %s, 
                    fechaHoraRegistro = now(), 
                    observacion = %s

                where SOLICITUD_SERVICIOid = %s, VEHICULOid = %s, CONDUCTORid = %s
                """
            #ejecutar la sentencia sql
            cursor.execute(sql, [self.latitud, self.longitud, self.nombreEstado, self.observacion, self.solicitud_servicio_id, self.vehiculo_id, self.conductor_id])

            #Confirmar la sentencia de ejecución
            con.commit()

            #retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'La actualización se ha registrado correctamente'})

        except con.Error as error:
            #Revocar la operación
            con.rollback()
            return json.dumps({'status': False, 'data': None, 'message': format(error)})

        finally:
            cursor.close()
            con.close()  
