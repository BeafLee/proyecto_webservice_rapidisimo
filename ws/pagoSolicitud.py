from flask import Blueprint, request, jsonify
from models.pagoSolicitud import PagoSolicitud
import json
import validarToken as vt

ws_pagoSolicitud = Blueprint("ws_pagoSolicitud", __name__)

@ws_pagoSolicitud.route('/solicitud/pago', methods = ["POST"])
#@vt.validar
def registrarPago():

    if request.method == 'POST':
        if not any(key not in request.form for key in ['solicitud_id', 'nombre_entidad', 'num_operacion', 'voucher']):
            return jsonify({'status': False, 'data': None, 'message': 'Falta parámetros'}), 400
        
        solicitud_id = request.form['solicitud_id']
        nombre_entidad = request.form['nombre_entidad']
        num_operacion = request.form['num_operacion']
        voucher = request.form['voucher']

        obj = PagoSolicitud(nombre_entidad=nombre_entidad, num_operacion=num_operacion)
    
        resultadoJSON = obj.registrarPago(solicitud_id, voucher)

        resultado = json.loads(resultadoJSON)

        if resultado['status'] == True: 
            return jsonify(resultado), 200
        else: 
            return jsonify(resultado), 500 #Reset Content