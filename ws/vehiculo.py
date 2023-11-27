from flask import Blueprint, request, jsonify
from models.vehiculo import Vehiculo
import json
import validarToken as vt

ws_vehiculo = Blueprint('ws_vehiculo',__name__)
@ws_vehiculo.route('/vehiculo/insertar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'matricula' not in request.form or 'capacidad_total' not in request.form or 'tipo_carga' not in request.form or 'modelo' not in request.form or 'marca' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400

    matricula = request.form['matricula']
    capacidad_total = request.form['capacidad_total']    
    tipo_carga = request.form['tipo_carga']
    modelo = request.form['modelo']
    marca = request.form['marca']

    obj=Vehiculo(None, matricula, capacidad_total, tipo_carga, modelo, marca)
    resultadoJSON=obj.registrarVehiculo()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401

@ws_vehiculo.route('/vehiculo', methods = ["GET"])
#@vt.validar
def listar():

    if request.method == 'GET':
        obj = Vehiculo()
    
        resultadoJSON = obj.listadoVehiculos()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content