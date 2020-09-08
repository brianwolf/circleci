from enum import Enum
from uuid import UUID

from flask import Blueprint, jsonify, request

from logic.app.models.ejemplo import Modelo
from logic.app.services import ejemplo_service
from logic.libs.excepcion.excepcion import AppException

blue_print = Blueprint('ejemplos', __name__, url_prefix='/api/v1/ejemplos')


class Errors(Enum):
    PRUEBA: 'PRUEBA'


@blue_print.route('/<uuid>', methods=['GET'])
def buscar(uuid):
    modelo = ejemplo_service.buscar(UUID(uuid))

    if not modelo:
        return '', 204

    return jsonify(modelo.to_dict())


@blue_print.route('', methods=['POST'])
def crear():
    modelo = Modelo.from_dict(request.json)
    uuid = ejemplo_service.crear(modelo)

    respuesta = {'id': str(uuid)}

    return jsonify(respuesta), 201


@blue_print.route('/<uuid>', methods=['DELETE'])
def borrar(uuid):
    return jsonify(ejemplo_service.borrar(UUID(uuid)))


@blue_print.route('/<uuid>', methods=['PUT'])
def modificar(uuid):
    modelo = Modelo.from_dict(request.json)
    return jsonify(ejemplo_service.modificar(UUID(uuid), modelo))


@blue_print.route('/todos', methods=['GET'])
def obtener_todos():
    return jsonify(ejemplo_service.obtener_todos())
