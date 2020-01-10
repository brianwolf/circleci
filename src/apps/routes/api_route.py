from fastapi import APIRouter
from starlette.status import *

import apps.configs.variables as var
from apps.configs.loggers import get_logger
from apps.models.errores import AppException

logger = get_logger()

router = APIRouter()
_prefix = ""


@router.get('/variables')
async def variables():
    respuesta = {}
    for key in var.mapa_variables.keys():
        respuesta[key] = var.get(key)

    return respuesta


@router.get('/errores', status_code=HTTP_409_CONFLICT)
async def error():
    raise AppException('PRUEBA', 'Rompamos todo, vieja!')


@router.get('/')
async def vivo():
    logger.info("VIVO")
    return {"estado": "vivo"}
