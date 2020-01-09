import json
import os

from flask import Flask, jsonify

import src.configs.variables as var
from src.utils.carga_dinamica_blue_prints import registrar_blue_prints

PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))

app = Flask(__name__)

registrar_blue_prints(app, 'src/routes')

if __name__ == "__main__":
    app.run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
