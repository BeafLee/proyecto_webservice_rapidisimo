from flask import Blueprint, request, jsonify
from models.estadoSolicitud import EstadoSolicitud
import json
import validarToken as vt

ws_estadoSolicitud = Blueprint("ws_estadoSolicitud", __name__)

@ws_estadoSolicitud.route('/solicitud/<int:idSolicitud>/estados', methods = ["GET"])
#@vt.validar
def registrarPago(idSolicitud):

    if request.method == 'GET':
        if not idSolicitud:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        obj = EstadoSolicitud()
    
        resultadoJSON = obj.listadoEstados(idSolicitud)

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content