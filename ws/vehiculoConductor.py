from flask import Blueprint, request, jsonify
from models.vehiculoConductor import VehiculoConductor
import json
import validarToken as vt

ws_vehiculoConductor = Blueprint("ws_vehiculoConductor", __name__)

@ws_vehiculoConductor.route('/solicitud/ubicacion', methods = ["POST"])
#@vt.validar
def listarUbicacion():

    if request.method == 'POST':
        if 'idSolicitud' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400

        idSolicitud = request.form['solicitud_id']

        obj = VehiculoConductor(solicitud_servicio_id = idSolicitud)
    
        resultadoJSON = obj.listado()

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
        
@ws_vehiculoConductor.route('/vehiculo/estado', methods = ["POST"])
#@vt.validar
def actualizarEstadoVehiculo():

    if request.method == 'POST':
        if not any(key not in request.form for key in ['solicitud_servicio_id', 'vehiculo_id', 'conductor_id', 'latitud', 'longitud', 'nombre_estado', 'observacion']):
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        solicitud_servicio_id = request.form['solicitud_servicio_id']
        vehiculo_id = request.form['vehiculo_id']
        conductor_id = request.form['conductor_id']
        latitud = request.form['latitud']
        longitud = request.form['longitud']
        nombre_estado = request.form['nombre_estado']
        observacion = request.form['observacion']

        obj = VehiculoConductor(solicitud_servicio_id=solicitud_servicio_id, vehiculo_id=vehiculo_id, conductor_id=conductor_id, latitud=latitud, longitud=longitud, nombreEstado=nombre_estado, observacion=observacion)
    
        resultadoJSON = obj.actualizarEstado()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content