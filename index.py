from flask import Flask
from ws.cliente import ws_cliente
from ws.sesion import ws_session
from ws.tarifa import ws_tarifa
from ws.solicitud import ws_solicitud
from ws.estado_solicitud import ws_estado_solicitud
#Importar a los módulos que contienen a los servicios web
from ws.pagoSolicitud import ws_pagoSolicitud
from ws.cliente import ws_cliente
from ws.estadoSolicitud import ws_estadoSolicitud
from ws.vehiculoConductor import ws_vehiculoConductor
from ws.conductor import ws_conductor 
from ws.vehiculo import  ws_vehiculo

#Crear la variable de aplicación con Flask
app = Flask(__name__)


#Registrar los módulos que contienen a los servicios web
app.register_blueprint(ws_pagoSolicitud)
app.register_blueprint(ws_cliente)
app.register_blueprint(ws_estadoSolicitud)
app.register_blueprint(ws_vehiculoConductor)
app.register_blueprint(ws_session)
app.register_blueprint(ws_tarifa)
app.register_blueprint(ws_solicitud)
app.register_blueprint(ws_estado_solicitud)
app.register_blueprint(ws_conductor)
app.register_blueprint(ws_vehiculo)
@app.route('/')
def home():
    return 'Servicios web Rapidisimo en ejecución'

#Iniciar el servicio web con Flask
if __name__ == '__main__':
    app.run(port=3008, debug=True, host='0.0.0.0')
