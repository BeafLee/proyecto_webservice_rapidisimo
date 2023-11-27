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
        
ws_solicitud = Blueprint('ws_solicitud',__name__)
@ws_solicitud.route('/solicitud/listaratencion/<string:tipo_doc>', methods=['GET'])
@vt.validar
def listarSolicitudAtencion(tipo_doc):
    if request.method == 'GET':
        obj = Solicitud()
        resultadoJSON = obj.listarSolicitudAtencion(tipo_doc)
        resultadoJSONObject = json.loads(resultadoJSON)
        if resultadoJSONObject['status'] == True:
            return jsonify(resultadoJSONObject), 200 #OK
        else:
            return jsonify(resultadoJSONObject), 205  #Recurso no encontrado

ws_solicitud = Blueprint('ws_solicitud',__name__)
@ws_solicitud.route('/solicitud/insertar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'nombres' not in request.form or 'direccion' not in request.form or 'email' not in request.form or 'usuario_id' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400
    
    descripcionCarga = request.form['descripcionCarga']
    claseCarga = request.form['claseCarga']    
    tipoCarga = request.form['tipoCarga']
    categoriaCarga = request.form['categoriaCarga']
    pesoKg = request.form['pesoKg']
    fechaHoraPartida = request.form['fechaHoraPartida']
    fechaHoraLlegada = request.form['fechaHoraLlegada']
    direccionOrigen = request.form['direccionOrigen']
    direccionDestino = request.form['direccionDestino']
    montoPagar = request.form['montoPagar']
    distanciaKm = request.form['fechaHoraPartida']
    TARIFAid = request.form['fechaHoraLlegada']
    CLIENTEid = request.form['direccionOrigen']
    PAGO_SOLICITUDid = request.form['direccionDestino']
  
    obj=Solicitud(None,descripcionCarga,claseCarga,tipoCarga,categoriaCarga,pesoKg,fechaHoraPartida,fechaHoraLlegada,direccionOrigen,direccionDestino,montoPagar,distanciaKm,TARIFAid,CLIENTEid,PAGO_SOLICITUDid)
    resultadoJSON=obj.registrarCliente()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401