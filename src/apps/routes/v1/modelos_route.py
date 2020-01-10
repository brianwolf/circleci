from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import *
from apps.models.modelos import Modelo

router = APIRouter()
_prefix = '/modelos'


@router.get('/{nombre}')
def probando(nombre, response: Response):

    if nombre == 'boom':
        response.status_code = HTTP_500_INTERNAL_SERVER_ERROR
        return {'BOOOM...!!!!': 'te lo dije'}

    return {'no pongas': 'boom'}

@router.post("/test")
def create_item(modelo: Modelo):
    return modelo
