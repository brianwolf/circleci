from fastapi import FastAPI
from starlette.requests import Request

from apps.configs.loggers import get_logger
from apps.models.errores import AppException

logger = get_logger()
app = APIRouter()


@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    get_logger().exception(str(e))
    return '', 500


@app.exception_handler(AppException)
def handle_business_exception(ae):
    return ae.respuesta_json()
