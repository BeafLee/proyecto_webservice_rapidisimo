from flask import Blueprint, request, jsonify
from models.conductor import Conductor
import json
import validarToken as vt

ws_conductor = Blueprint('ws_conductor',__name__)
@ws_conductor.route('/conductor/insertar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'tipoDoc' not in request.form or 'numeroDoc' not in request.form or 'apellidos' not in request.form or 'nombres' not in request.form or 'direccion' not in request.form or 'fechaNac' not in request.form or 'estado' not in request.form or 'usuario_id' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400

    tipoDoc = request.form['tipoDoc']
    numeroDoc = request.form['numeroDoc']
    apellidos = request.form['apellidos']    
    nombres = request.form['nombres']
    direccion = request.form['direccion']
    fechaNac = request.form['fechaNac']
    estado = request.form['estado']
    usuarioid = request.form['usuario_id']

    obj=Conductor(None, tipoDoc, numeroDoc, apellidos, nombres, direccion, fechaNac, estado, usuarioid)
    resultadoJSON=obj.registrarConductor()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401

@ws_conductor.route('/conductor', methods = ["GET"])
#@vt.validar
def listar():

    if request.method == 'GET':
        obj = Conductor()
    
        resultadoJSON = obj.listadoConductores()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content