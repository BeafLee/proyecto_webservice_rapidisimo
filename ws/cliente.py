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
    if request.method != 'POST':
        return jsonify({'status': False, 'data': None, 'message': 'Método no permitido'}), 405

    if 'tipoDoc' not in request.form:
        return jsonify({'status': False, 'data': None, 'message': 'Falta parámetro tipoDoc'}), 400

    tipoDoc = request.form['tipoDoc']
    numDoc = request.form.get('numDoc')
    direccion = request.form.get('direccion')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    estado = request.form.get('estado')
    usuarioid = request.form.get('usuario_id')

    if tipoDoc == 'DNI':
        if not all([numDoc, direccion, email, usuarioid]):
            return jsonify({'status': False, 'data': None, 'message': 'Faltan parámetros para DNI'}), 400
        nombres = request.form.get('nombres')
        obj = Cliente(None, tipoDoc, numDoc, nombres, None, direccion, email, telefono, estado, usuarioid)
    else:
        if not all([numDoc, direccion, email, usuarioid]):
            return jsonify({'status': False, 'data': None, 'message': 'Faltan parámetros para tipoDoc distinto a DNI'}), 400
        razonSocial = request.form.get('razonSocial')
        obj = Cliente(None, tipoDoc, numDoc, None, razonSocial, direccion, email, telefono, estado, usuarioid)

    resultadoJSON = obj.registrarCliente()
    resultadoJSONObject = json.loads(resultadoJSON)

    if resultadoJSONObject['status']:
        return jsonify(resultadoJSONObject), 200
    else:
        return jsonify(resultadoJSONObject), 401


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

from flask import request

@ws_cliente.route('/cliente/listar', methods=['GET'])
def filtrarclientes():
    if request.method == 'GET':
        obj = Cliente()

        # Obtener el tipo de filtro y su valor desde los parámetros de la solicitud
        tipo_filtro = request.args.get('tipo_filtro', None)

        # Validar que se proporcionen tanto el tipo como el valor del filtro
        if tipo_filtro is None:
            return jsonify({'error': 'Se debe proporcionar el tipo de filtro'}), 400

        # Realizar el listado según el tipo de filtro
        if tipo_filtro == 'DNI':
            resultadoJSON = obj.listadoClientesDNI()
        elif tipo_filtro == 'RUC':
            resultadoJSON = obj.listadoClientesRUC()
        elif tipo_filtro == 'nombres':
            resultadoJSON = obj.listadoClientesNombre()
        elif tipo_filtro == 'estado':
            resultadoJSON = obj.listadoClientesEstado()
        else:
            return jsonify({'error': 'Tipo de filtro no válido'}), 400

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True:
            return jsonify(resultado), 200
        else:
            return jsonify(resultado), 500  # Reset Content
        
#/cliente/listar?tipo_filtro=DNI&valor_filtro=11111111
#/cliente/listar?tipo_filtro=RUC&valor_filtro=22222222
#/cliente/listar?tipo_filtro=nombres&valor_filtro=Cliente1
#/cliente/listar?tipo_filtro=estado&valor_filtro=A
        
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