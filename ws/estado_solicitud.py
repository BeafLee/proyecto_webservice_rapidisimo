from flask import Blueprint, request, jsonify
from models.estado_solicitud import Estado
from config import SecretKey
import json
import jwt
import datetime
import validarToken as vt
#Generar un Blueprint para el inicio de la sesion
ws_estado_solicitud = Blueprint('ws_estado_solicitud',__name__)
@ws_estado_solicitud.route('/estado/registrar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'estado' not in request.form or 'observacion' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400
        #Leer el parametro de entrada
    estado = request.form['estado']
    observacion = request.form['observacion']
    #Instanciar a la clase cliente
    obj=Estado(None,estado,None,observacion)
    resultadoJSON=obj.registrar_estado()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401