from conexionBD import Conexion as db
import json

class Cliente:
    def __init__(self, id_cliente=None, tipo_doc=None, numero_doc=None, nombres=None, razon_social=None, direccion=None, email=None, telefono=None, estado=None, usuario_id=None):
        self.id_cliente = id_cliente
        self.tipo_doc = tipo_doc
        self.numero_doc = numero_doc
        self.nombres = nombres
        self.razon_social = razon_social
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
        self.estado = estado
        self.usuario_id = usuario_id

    def listadoClientes(self):
        con = db().open

        cursor = con.cursor()

        sql = """
            SELECT * 
            FROM cliente
            """
        
        cursor.execute(sql)

        datos = cursor.fetchall()

        cursor.close()
        con.close()

        if datos:
            return json.dumps({'status': True, 'data': datos, 'message': 'Lista de los clientes'})
        else:
            return json.dumps({'status': False, 'data': [], 'message': 'Sin registros'})
        

    def actualizarEstado(self):
        #Abrimos conexion a la bd
        con = db().open
    
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit = False

        #Crear un cursor
        cursor = con.cursor()

        #Preparar la sentencia para actualizar el token
        sql = "update cliente set estado = %s where id = %s"

        try:
            #ejecutar la sentencia sql
            cursor.execute(sql, [self.estado, self.id])
            #Confirmar la sentencia de ejecución
            con.commit()

            #retornar un mensaje
            return json.dumps({'status': True, 'data': None, 'message': 'Estado de cliente actualizado correctamente'})

        except con.Error as error:
            #Revocar la operación
            con.rollback()
            return json.dumps({'status': False, 'data': None, 'message': format(error)})

        finally:
            cursor.close()
            con.close()

    def registrarCliente(self):
        #Abrir conexion a la bd
        con=db().open 
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit=False
        cursor=con.cursor()
        #Preparar la sentencia para actualizar el token
        if self.tipoDoc=='DNI':
            sql="""insert into cliente(tipoDoc,numeroDoc,nombres,direccion,email,telefono,estado,usuarioid) 
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        else:
            sql="""insert into cliente(tipoDoc,numeroDoc,razonSocial,direccion,email,telefono,estado,usuarioid) 
                    values(%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            #Ejecutra la sentencia sql
            if self.tipoDoc=='DNI':
                cursor.execute(sql,[self.tipoDoc,self.numeroDoc,self.nombres,self.direccion,self.email,self.telefono,self.estado,self.usuarioid])
                con.commit()
            else:
                cursor.execute(sql,[self.tipoDoc,self.numeroDoc,self.razonSocial,self.direccion,self.email,self.telefono,self.estado,self.usuarioid])
                con.commit()
            return json.dumps({'status':True,'data':None,'message':'Cliente registrado correctamente'})
        except con.Error as error:
            con.rollback()
            return json.dumps({'status':False,'data':None,'message':format(error)})
        finally:
            cursor.close()
            con.close()