import app.configs.variables as var

from typing import List
from app.configs.loggers import get_logger
from app.configs.mongo import cliente
from app.models.modelos import ModeloDocument
from app.models.errores import ErrorApp
from uuid import UUID
from datetime import datetime
from mongoengine import NotUniqueError, DoesNotExist

RAMA_MODELOS = var.get('RAMA_MODELOS')

db = cliente.get_collection(RAMA_MODELOS)


def guardar(modelo_document: ModeloDocument) -> UUID:
    '''
    Guarda un modelo en la base de datos
    '''
    try:
        return modelo_document.save().id

    except NotUniqueError as nue:
        mensaje = f'El nombre {modelo_document.nombre} ya esta en uso'
        raise ErrorApp('NOMBRE_EXISTENTE', mensaje)


def buscar(filtros: ModeloDocument) -> List[ModeloDocument]:
    '''
    Busca modelos en la base de datos segun los parametros especificados en el objeto filtros
    '''
    resultado = db.find(filtros.to_mongo())
    return resultado


def buscar_por_id(id: UUID) -> ModeloDocument:
    '''
    Busca un modelo por una id
    '''
    return ModeloDocument.objects.get(id=id)


def buscar_por_nombre(nombre: str) -> ModeloDocument:
    '''
    Busca un modelo por una id
    '''
    try:
        return ModeloDocument.objects.get(nombre=nombre)
    except DoesNotExist as e:
        mensaje = f'El modelo {nombre} no fue encontrado'
        raise ErrorApp('MODELO_NO_ENCONTRADO', mensaje)


def borar_por_id(id: UUID):
    '''
    Borra un modelo por una id
    '''
    modelo = buscar_por_id(id)
    modelo.delete()
