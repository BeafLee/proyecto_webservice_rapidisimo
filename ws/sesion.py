from flask import Blueprint, request, jsonify
from models.sesion import Sesion
from config import SecretKey
import json
import jwt
import datetime

#Generar un Blueprint para el inicio de la sesion
ws_session = Blueprint('ws_session',__name__)
#Crear una ruta(endpoint)
@ws_session.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        if 'usuario' not in request.form or 'clave' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Faltan parametro'})
        usuario=request.form['usuario']
        clave=request.form['clave']
        obj=Sesion(usuario,clave)
        resultadoJSON=obj.iniciarSesion()
        
        #convertir el resultado a json
        resultadoJSONObject=json.loads(resultadoJSON) 
        
        #Mostrar el resultado
        if(resultadoJSONObject['status']==True):
            #Obtener el id del usuario
            usuarioID=resultadoJSONObject['data']['id']
            token=jwt.encode({'usuarioID':usuarioID,'exp':datetime.datetime.utcnow()+datetime.timedelta(seconds=60*60*3)},SecretKey.JWT_SECRET_KEY)
            
            
        #Incluir al token dentro del resultado
        resultadoJSONObject['data']['token']= token
        #Actualizar el token generado en la base de datos
        obj.actualizarToken(token,usuarioID)
        #imprimir el resultado
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401
                   