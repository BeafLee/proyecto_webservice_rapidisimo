from flask import Blueprint, request, jsonify
from models.solicitud import Solicitud
from config import SecretKey
import json
import jwt
import datetime
import validarToken as vt
ws_solicitud = Blueprint('ws_solicitud',__name__)
@ws_solicitud.route('/solicitud/listar/<int:id>', methods=['GET'])
@vt.validar
def listarsolicitud(id):
    if request.method == 'GET':
        #Instanciar a la clase Cliente
        obj = Solicitud()
        #Ejecutar al método eliminar()
        resultadoJSON = obj.listarSolicitud(id)
        #Convertir el resultado JSON(String) a JSON(Object)
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado