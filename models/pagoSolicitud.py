from conexionBD import Conexion as db
import os
import uuid
import json
import base64
from util import CustomJsonEncoder

class PagoSolicitud:
    def __init__(self, id_pago=None, nombre_entidad=None, num_operacion=None, fecha_hora_operacion=None, url_voucher=None):
        self.id_pago = id_pago
        self.nombre_entidad = nombre_entidad
        self.num_operacion = num_operacion
        self.fecha_hora_operacion = fecha_hora_operacion
        self.url_voucher = url_voucher

    def registrarPago(self, idSolicitud, imagenBase64):
        #Abrimos conexion a la bd
        con = db().open
    
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        try:
            idCliente = 1
            
            #Almacenar la imagen (Base64) del voucher y que nos retorne la url
            rutaCarpeta = os.path.join('/static/cliente/' + str(idCliente))
            if not os.path.exists(rutaCarpeta):
                os.makedirs(rutaCarpeta)

            imgNombre = str(uuid.uuid4())

            rutaImagen = os.path.join(rutaCarpeta, imgNombre)
            with open(rutaImagen, 'wb') as f:
                f.write(base64.b64decode(imagenBase64))

            print('ruta imagen almacenada: ', rutaImagen)

            #Consulta para registrar el pago
            sql = "insert into PAGO_SOLICITUD(nombreEntidad, numOperacion, fechaHoraOperacion, urlVoucher) values (%s,%s, now(),%s)"

            #ejecutar la sentencia sql
            cursor.execute(sql, [self.nombre_entidad, self.num_operacion, rutaImagen])

            idPago = cursor.lastrowid

            #Consulta para registrar el id del pago registrado a la solicitud
            sql = "update SOLICITUD_SERVICIO set PAGO_SOLICITUDid = %s where id = %s"

            #ejecutar la sentencia sql
            cursor.execute(sql, [idPago, idSolicitud])

            #Confirmar la sentencia de ejecución
            con.commit()

            #retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Pago de solicitud registrado correctamente'})

        except con.Error as error:
            #Revocar la operación
            con.rollback()
            return json.dumps({'status': False, 'data': None, 'message': format(error)})

        finally:
            cursor.close()
            con.close()

    def estadoPago(self, solicitud_id):
        con = db().open

        cursor = con.cursor()

        sql = """
            SELECT E.estado, E.nombreEstado, P.id, P.nombreEntidad, P.numOperacion, P.fechaHoraOperacion, P.urlVoucher
            FROM PAGO_SOLICITUD P
            INNER JOIN SOLICITUD_SERVICIO S ON P.id = S.PAGO_SOLICITUDid
            INNER JOIN ESTADO_SOLICITUD E ON S.id = E.SOLICITUD_SERVICIOid
            WHERE E.nombreEstado = 'RECHAZADO' OR E.nombreEstado = 'CONFIRMADO' AND E.SOLICITUD_SERVICIOid = %s
            """
        
        cursor.execute(sql, [solicitud_id])

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Estado del pago'}, cls=CustomJsonEncoder)
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})

    #API 14
    def validarPago(self, solicitud_id, respuesta):
        #Abrimos conexion a la bd
        con = db().open
    
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        try:
            if (respuesta == "aceptar"):
                
                #Actualizar el estadoPago de la solicitud
                sql = "update SOLICITUD_SERVICIO set estadoPago = 'C' where id = %s"

                #ejecutar la sentencia sql
                cursor.execute(sql, [solicitud_id])

            else:

                #Eliminar la relación del pago rechazado
                sql = "update SOLICITUD_SERVICIO set estadoPago = 'R' where id = %s"

                #ejecutar la sentencia sql
                cursor.execute(sql, [solicitud_id])

            #Confirmar la sentencia de ejecución
            con.commit()

            #retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Verificación registrado correctamente'})

        except con.Error as error:
            #Revocar la operación
            con.rollback()
            return json.dumps({'status': False, 'data': None, 'message': format(error)})

        finally:
            cursor.close()
            con.close()