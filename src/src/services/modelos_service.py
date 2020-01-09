from uuid import UUID

import src.configs.variables as var
from src.configs.loggers import get_logger
from src.models.errores import AppException
from src.models.modelos import Modelo


def guardar(modelo: Modelo) -> UUID:
    '''
    Ejemplo de guardado
    '''
    id_generada = UUID()
    return id_generada


def buscar(id: UUID) -> Modelo:
    '''
    Ejemplo busqueda
    '''
    return Modelo('modelo')
