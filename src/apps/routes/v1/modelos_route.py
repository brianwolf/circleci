from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import *

router = APIRouter()
_prefix = '/modelos'


@router.get('/{nombre}')
def probando(nombre, response: Response):

    if nombre == 'boom':
        response.status_code = HTTP_500_INTERNAL_SERVER_ERROR
        return {'BOOOM...!!!!': 'te lo dije'}

    return {'no pongas': 'boom'}
