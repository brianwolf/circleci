from uuid import UUID

import app.configs.variables as var
from app.configs.loggers import get_logger
from app.models.errores import ErrorApp
from app.models.modelos import Modelo


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
