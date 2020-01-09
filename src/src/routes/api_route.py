from flask import Blueprint, jsonify, request

import src.configs.variables as var
import src.services.modelos_service as modelos
from src.configs.loggers import get_logger
from src.models.errores import AppException
from src.models.modelos import Modelo

blue_print = Blueprint('errors', __name__, url_prefix='')

logger = get_logger()


@blue_print.route('/variables')
def variables():
    respuesta = {}
    for key in var.mapa_variables.keys():
        respuesta[key] = var.get(key)

    return jsonify(respuesta)


@blue_print.route('/error')
def error():
    raise AppException('PRUEBA', 'Rompimos todo vieja!')


@blue_print.route('/')
def vivo():
    logger.info("VIVO")
    respuesta = {"estado": "vivo"}
    return jsonify(respuesta)
