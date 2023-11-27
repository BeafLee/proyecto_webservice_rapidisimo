from flask import Blueprint, request, jsonify
from models.solicitud import Solicitud
from config import SecretKey
import json
import jwt
import datetime
import validarToken as vt
ws_solicitud = Blueprint('ws_solicitud',__name__)
@ws_solicitud.route('/solicitud/listar/<int:id>', methods=['GET'])
#@vt.validar
def listarSolicitud(id):
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
        
@ws_solicitud.route('/solicitud/listaratencion/<string:tipo_doc>', methods=['GET'])
#@vt.validar
def listarSolicitudAtencion(tipo_doc):
    if request.method == 'GET':
        obj = Solicitud()
        resultadoJSON = obj.listarSolicitudAtencion(tipo_doc)
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado


@ws_solicitud.route('/solicitud/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
        # Verifica que los parámetros necesarios estén presentes en el formulario
        if 'descripcionCarga' not in request.form or 'claseCarga' not in request.form or 'tipoCarga' not in request.form or 'categoriaCarga' not in request.form or 'pesoKg' not in request.form or 'fechaHoraPartida' not in request.form or 'fechaHoraLlegada' not in request.form or 'direccionOrigen' not in request.form or 'direccionDestino' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Faltan parámetros'}), 400

        descripcionCarga = request.form['descripcionCarga']
        claseCarga = request.form['claseCarga']
        tipoCarga = request.form['tipoCarga']
        categoriaCarga = request.form['categoriaCarga']
        pesoKg = float(request.form['pesoKg'])
        fechaHoraPartida = request.form['fechaHoraPartida']
        fechaHoraLlegada = request.form['fechaHoraLlegada']
        source = request.form['direccionOrigen']
        destination = request.form['direccionDestino']
        TARIFAid = int(request.form['TARIFAid'])
        CLIENTEid = int(request.form['CLIENTEid'])
        PAGO_SOLICITUDid = int(request.form['PAGO_SOLICITUDid'])

        obj = Solicitud(
            None, descripcionCarga, claseCarga, tipoCarga, categoriaCarga, pesoKg,
            fechaHoraPartida, fechaHoraLlegada, source, destination,
            None, None, TARIFAid, CLIENTEid, PAGO_SOLICITUDid 
        )

        # Llama al método registrarSolicitud
        resultadoJSON = obj.registrarSolicitud(source, destination)

        # Procesa el resultado y responde según sea necesario
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200
        else:
            return jsonify(resultadoJSONObject), 401
        


@ws_solicitud.route('/solicitud/detalle/<int:id>', methods=['GET'])
#@vt.validar
def listarSolicitudAtencion(id):
    if request.method == 'GET':
        obj = Solicitud(p_id=id)
        resultadoJSON = obj.obtenerDetalleSolicitud()
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado



@ws_solicitud.route('/solicitud/conductor', methods=['POST'])
def listarPorConductor():
    if request.method == 'POST':
        # Verifica que los parámetros necesarios estén presentes en el formulario
        if 'conductor_id' not in request.form:
            return jsonify({'status': False, 'data': None, 'message': 'Faltan parámetros'}), 400

        conductor_id = request.form['conductor_id']

        obj = Solicitud()

        # Llama al método registrarSolicitud
        resultadoJSON = obj.listarSolicitudConductor(conductor_id)

        # Procesa el resultado y responde según sea necesario
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200
        else:
            return jsonify(resultadoJSONObject), 401
        