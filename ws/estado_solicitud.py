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
        if 'observacion' not in request.form or 'nombreEstado' not in request.form or 'solicitudid' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400
        #Leer el parametro de entrada
    nombreEstado = request.form['nombreEstado']
    observacion = request.form['observacion']
    solicitud_servicio = request.form['solicitudid']
    #Instanciar a la clase cliente
    obj=Estado(None,nombreEstado,None,observacion,None,solicitud_servicio)
    resultadoJSON=obj.registrar_estado()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401
