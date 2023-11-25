from flask import Flask
from ws.cliente import ws_cliente
from ws.sesion import ws_session
#Importar a los módulos que contienen a los servicios web
#from ws.sesion import ws_sesion

#Crear la variable de aplicación con Flask
app = Flask(__name__)


#Registrar los módulos que contienen a los servicios web
app.register_blueprint(ws_session)
app.register_blueprint(ws_cliente)
@app.route('/')
def home():
    return 'Servicios web Rapidisimo en ejecución'

#Iniciar el servicio web con Flask
if __name__ == '__main__':
    app.run(port=3008, debug=True, host='0.0.0.0')
