from flask import Blueprint, request, jsonify
from models.cliente import Cliente
import json
import validarToken as vt

ws_cliente = Blueprint("ws_cliente", __name__)

@ws_cliente.route('/cliente', methods = ["GET"])
#@vt.validar
def listarUbicacion():

    if request.method == 'GET':
        obj = Cliente()
    
        resultadoJSON = obj.listado()

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