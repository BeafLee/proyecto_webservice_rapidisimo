from ast import arg
from flask import jsonify, request
from functools import wraps
from config import SecretKey
import jwt
#from models.sesion import Sesion
import json

def validar(fx): ## Funcion de envoltura 
    @wraps(fx)
    def envoltura(*args, **kwargs):
        if not request.headers.get("Authorization"):
            return jsonify({"status": False, "data": None, "message": "Falta el token"}), 403 #
        
        token = request.headers.get("Authorization").split('Bearer ')[1] #Obtener el token del encabezado de la solicitud, el Split elimina al Bearer del token
        
        try:
            #Decodificar el token
            token_decode = jwt.decode(token, SecretKey.JWT_SECRET_KEY, algorithms="HS256")

            #Extraer el id del usuario
            usuarioID = token_decode["usuarioID"]


            estado_token_BD = validarEstadoTokenUsuario(usuarioID)
            if not estado_token_BD:
                return jsonify({"status": False, "data": None, "message": "El token se encuentra inactivo"})

        except jwt.DecodeError as err:
            return jsonify({"status": False, "data": None, "message": "Error al codificar el token", "internal_message": format(err)}), 403
        
        except jwt.ExpiredSignatureError as err:
            return jsonify({"status": False, "data": None, "message": "El token ha expirado", "internal_message": format(err)}), 403
        
        except jwt.InvalidTokenError as err:
            return jsonify({"status": False, "data": None, "message": "Token invalido", "internal_message": format(err)}), 403

        return fx(*args, **kwargs)
    
    return envoltura


def validarEstadoTokenUsuario(usuarioID):
    obj = Sesion()
    resultadoJSON = obj.validarEstadoToken(usuarioID)
    resultado = json.loads(resultadoJSON)
    if resultado['status'] == True:
        estado_token_BD = resultado['data']['estado_token']
        if estado_token_BD == None:
            return False
        elif estado_token_BD == '0':
            return False
        else:
            return True
        
    else:
        return False