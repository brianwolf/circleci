import json
import os

from flask import Flask, jsonify

import app.configs.variables as var
from app.configs.loggers import get_logger
from app.models.errores import ErrorApp
from app.utils.carga_dinamica_blue_prints import registrar_blue_prints

NOMBRE_LOGGER_REST = var.get('NOMBRE_LOG_REST')
PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))

app = Flask(__name__)

logger = get_logger()


@app.errorhandler(Exception)
def handle_exception(e):
    get_logger().exception(str(e))
    return '', 500


@app.errorhandler(ErrorApp)
def handle_exception(ae):
    return ae.respuesta_json()


@app.route('/')
def vivo():
    logger.info("VIVO")
    respuesta = {"estado": "vivo"}
    return jsonify(respuesta)


@app.route('/variables')
def variables():
    respuesta = {}
    for key in var.mapa_variables.keys():
        respuesta[key] = var.get(key)

    return jsonify(respuesta)


DIRECTORIO_RUTAS = 'app/routes'
registrar_blue_prints(app, DIRECTORIO_RUTAS)

if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
