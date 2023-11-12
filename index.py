from flask import Flask

#Importar a los módulos que contienen a los servicios web
from ws.pagoSolicitud import ws_pagoSolicitud
from ws.cliente import ws_cliente
from ws.estadoSolicitud import ws_estadoSolicitud
from ws.vehiculoConductor import ws_vehiculoConductor

#Crear la variable de aplicación con Flask
app = Flask(__name__)


#Registrar los módulos que contienen a los servicios web
app.register_blueprint(ws_pagoSolicitud)
app.register_blueprint(ws_cliente)
app.register_blueprint(ws_estadoSolicitud)
app.register_blueprint(ws_vehiculoConductor)

@app.route('/')
def home():
    return 'Servicios web Rapidisimo en ejecución'

#Iniciar el servicio web con Flask
if __name__ == '__main__':
    app.run(port=3008, debug=True, host='0.0.0.0')
