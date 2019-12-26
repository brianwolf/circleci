from flask import Blueprint, jsonify, request

import app.configs.variables as var
import app.services.modelos_service as modelos
from app.configs.loggers import get_logger
from app.models.errores import ErrorApp
from app.models.modelos import Modelo

blue_print = Blueprint('modelos', __name__, url_prefix='/api/v1/modelos')


@blue_print.route('/<id>', methods=['GET'])
def buscar(id):

    modelo = modelos.buscar(id)
    return jsonify(modelo.to_dict())


@blue_print.route('', methods=['POST'])
def guardar():

    modelo = Modelo(**request.json)
    id = modelos.guardar(modelo)

    respuesta = {'id': str(id)}

    return jsonify(respuesta), 201
