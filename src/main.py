import json
import os

from flask import Flask, jsonify

import app.configs.variables as var
from app.configs.loggers import get_logger
from app.models.errores import AppException
from app.utils.carga_dinamica_blue_prints import registrar_blue_prints
from app.configs.error_handlers import error_handler_bp


PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))


logger = get_logger()

app = Flask(__name__)
app.register_blueprint(error_handler_bp)

registrar_blue_prints(app, 'app/routes')


if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
