from flask import Blueprint, request, jsonify
from models.cliente import Cliente
from config import SecretKey
import json
import jwt
import datetime
import validarToken as vt
#Generar un Blueprint para el inicio de la sesion
ws_cliente = Blueprint('ws_cliente',__name__)
@ws_cliente.route('/cliente/insertar', methods=['POST'])
@vt.validar
def insertar():
    if request.method == 'POST':
        if 'nombres' not in request.form or 'direccion' not in request.form or 'email' not in request.form or 'usuario_id' not in request.form:
            return jsonify({'status': False,'data':None,'message':'Falta parametros'}),400
        #Leer el parametro de entrada
    tipoDoc = request.form['tipoDoc']
    numDoc = request.form['numDoc']    
    nombres = request.form['nombres']
    razonSocial = request.form['razonSocial']
    direccion = request.form['direccion']
    email = request.form['email']
    telefono = request.form['telefono']
    estado = request.form['estado']
    usuarioid = request.form['usuario_id']
    #Instanciar a la clase cliente
    obj=Cliente(None,tipoDoc,numDoc,nombres,razonSocial,direccion,email,telefono,estado,usuarioid)
    resultadoJSON=obj.registrarCliente()
    resultadoJSONObject=json.loads(resultadoJSON)
    if(resultadoJSONObject['status']==True):
        return jsonify(resultadoJSONObject),200
    else:
        return jsonify(resultadoJSONObject),401

@ws_cliente.route('/cliente', methods = ["GET"])
#@vt.validar
def listar():

    if request.method == 'GET':
        obj = Cliente()
    
        resultadoJSON = obj.listadoClientes()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content
        

@ws_cliente.route('/cliente/estado', methods = ["POST"])
#@vt.validar
def registrarPago():

    if request.method == 'POST':
        if not any(key not in request.form for key in ['cliente_id', 'estado']):
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        cliente_id = request.form['cliente_id']
        estado = request.form['estado']

        obj = Cliente(id_cliente=cliente_id, estado=estado)
    
        resultadoJSON = obj.actualizarEstado()

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content