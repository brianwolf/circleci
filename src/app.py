import json
import os

from fastapi import FastAPI

import apps.configs.variables as var
import apps.routes.api_route as api_route
from apps.utils.carga_dinamica_rutas import registrar_ruta

PYTHON_HOST = var.get('PYTHON_HOST')
PYTHON_PORT = int(var.get('PYTHON_PORT'))

app = FastAPI()

registrar_ruta(app, 'apps/routes')

# if __name__ == "__main__":
#     app. run(host=PYTHON_HOST, port=PYTHON_PORT, debug=True)
