from enum import Enum
from typing import List
from uuid import UUID, uuid4

from apps.configs.loggers import get_logger
from apps.models.ejemplo import Modelo
from apps.models.errores import AppException

logger = get_logger()

_modelos: List[Modelo] = []


class Errores(Enum):
    MODELO_NO_ENCONTRADO = 'MODELO_NO_ENCONTRADO'


def crear(modelo: Modelo) -> UUID:
    '''
    Ejemplo de creacion
    '''
    uuid_generada = uuid4()
    modelo.uuid = uuid_generada

    _modelos.append(modelo)

    return uuid_generada


def buscar(uuid: UUID) -> Modelo:
    '''
    Ejemplo de busqueda
    '''
    for m in _modelos:
        if m.uuid == uuid:
            return m

    return None


def borrar(uuid: UUID) -> Modelo:
    '''
    Ejemplo de borrado
    '''
    modelo_a_borrar = buscar(uuid)

    if not modelo_a_borrar:
        logger.error('Modelo no encontrado al intentar borrar')
        mensaje = f'El modelo con id {uuid} no existe'
        raise AppException(Errores.MODELO_NO_ENCONTRADO, mensaje)

    _modelos.remove(modelo_a_borrar)

    return modelo_a_borrar


def modificar(uuid: UUID, modelo: Modelo) -> Modelo:
    '''
    Ejemplo de modificacion
    '''
    borrar(uuid)

    modelo.uuid = uuid
    _modelos.append(modelo)

    return modelo


def obtener_todos() -> List[Modelo]:
    '''
    Ejemplo para obtener todos los modelos
    '''
    return _modelos
