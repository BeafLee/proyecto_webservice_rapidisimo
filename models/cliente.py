from conexionBD import Conexion as db
import json
class Cliente():
    def __init__(self,p_id=None,p_tipodoc=None,p_numdoc=None,p_nombres=None,p_razonSocial=None,p_direccion=None,p_email=None,p_telefono=None,p_estado=None,p_usuarioid=None):
        self.id=p_id
        self.tipoDoc=p_tipodoc
        self.numeroDoc=p_numdoc
        self.nombres=p_nombres
        self.razonSocial=p_razonSocial
        self.direccion=p_direccion
        self.email=p_email
        self.telefono=p_telefono
        self.estado=p_estado
        self.usuarioid=p_usuarioid
        
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
    