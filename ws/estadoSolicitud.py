from flask import Blueprint, request, jsonify
from models.estadoSolicitud import EstadoSolicitud
import json
import validarToken as vt

ws_estadoSolicitud = Blueprint("ws_estadoSolicitud", __name__)

@ws_estadoSolicitud.route('/solicitud/estados', methods = ["POST"])
#@vt.validar
def registrarPago():

    if request.method == 'POST':
        if 'solicitud_id' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        idSolicitud = request.form['solicitud_id']

        obj = EstadoSolicitud(solicitud_servicio_id=idSolicitud)
    
        resultadoJSON = obj.listadoEstados()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content