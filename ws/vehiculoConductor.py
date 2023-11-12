from flask import Blueprint, request, jsonify
from models.vehiculoConductor import VehiculoConductor
import json
import validarToken as vt

ws_vehiculoConductor = Blueprint("ws_vehiculoConductor", __name__)

@ws_vehiculoConductor.route('/solicitud/<int:idSolicitud>/ubicacion', methods = ["GET"])
#@vt.validar
def listarUbicacion(idSolicitud):

    if request.method == 'GET':
        if not idSolicitud:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        obj = VehiculoConductor()
    
        resultadoJSON = obj.listadoPorSolicitud(idSolicitud)

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content
        

@ws_vehiculoConductor.route('/solicitud/asignar', methods = ["POST"])
#@vt.validar
def asignarVehiculo():

    if request.method == 'POST':
        if not any(key not in request.form for key in ['solicitud_servicio_id', 'vehiculo_id', 'conductor_id']):
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        solicitud_servicio_id = request.form['solicitud_servicio_id']
        vehiculo_id = request.form['vehiculo_id']
        conductor_id = request.form['conductor_id']

        obj = VehiculoConductor(solicitud_servicio_id=solicitud_servicio_id, vehiculo_id=vehiculo_id, conductor_id=conductor_id)
    
        resultadoJSON = obj.asignar()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content