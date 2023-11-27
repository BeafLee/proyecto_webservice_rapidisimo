from conexionBD import Conexion as db
import json

class Sesion():
    def __init__(self,p_usuario=None,p_clave=None):
        self.usuario = p_usuario
        self.clave = p_clave
    def iniciarSesion(self):
        con=db().open 
        cursor=con.cursor()
        sql="""SELECT id,tipoUsuario FROM USUARIO WHERE usuario=%s AND contrasena=%s"""
        cursor.execute(sql,[self.usuario,self.clave])
        datos=cursor.fetchone()
        cursor.close()
        con.close()
        
        #Devolver el resultado        
        if datos: #Validar si la variable datos contiene registros
            if datos['tipoUsuario']is not None:
                return json.dumps({'status':True,'data':datos,'message': 'Credenciales correctas. Bienvenido a la aplicacion.'})
            else:
                return json.dumps({'status':False,'data':None,'message':'Su cuenta esta inactiva. Consulte con su administrador.'})
        else:
            return json.dumps({'status':False,'data':None,'message':'El usuario no existe o sus credenciales son incorrectas.'})
    def actualizarToken(self,token,usuarioID):
        #Abrir conexion a la bd
        con=db().open 
        #Configurar para que los cambios de escritura en la BD se confirmen de manera manual
        con.autocommit=False
        cursor=con.cursor()
        #Preparar la sentencia para actualizar el token
        sql="UPDATE USUARIO set token=%s,estadoToken='A' where id=%s"
        try:
            #Ejecutra la sentencia sql
            cursor.execute(sql,[token,usuarioID])
            con.commit()
        except con.Error as error:
            con.rollback()
        finally:
            cursor.close()
            con.close()
    def validarEstadoToken(self,usuarioID):
        con=db().open 
        cursor=con.cursor()
        sql="select estadoToken from USUARIO where id=%s"
        cursor.execute(sql,[usuarioID])
        datos=cursor.fetchone()
        cursor.close()
        con.close()
        if datos: #Validar si la variable datos contiene registros
           return json.dumps({'status':True,'data':datos,'message': 'Estado de Token'})
        else:
            return json.dumps({'status':False,'data':None,'message':'Estado de Token no encontrado'})