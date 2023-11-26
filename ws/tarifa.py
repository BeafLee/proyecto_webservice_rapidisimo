from flask import Blueprint, request, jsonify
from models.tarifa import Tarifa
from config import SecretKey
import json
import jwt
import datetime
import validarToken as vt
ws_tarifa = Blueprint('ws_tarifa',__name__)
@ws_tarifa.route('/tarifa/insertar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'tarifa' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400
        #Leer el parametro de entrada
    tarifa = (request.form['tarifa'])
    #Instanciar a la clase cliente
    
    obj=Tarifa(None,tarifa)
    resultadoJSON=obj.registrarTarifa()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401
