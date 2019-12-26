import app.services.modelos_service as modelos
import app.configs.variables as var

from flask import jsonify, Blueprint, request
from app.configs.loggers import get_logger
from app.models.modelos import Modelo, Archivo
from app.models.errores import ErrorApp
from app.utils.archivos import nombre_extension

RAMA_MODELOS = var.get('RAMA_MODELOS')

blue_print = Blueprint('modelos', __name__, url_prefix='/api/v1/modelos')


@blue_print.route('/<id>', methods=['GET'])
def obtener(id):

    contenidos_tambien = request.args.get('base64') == 'true'

    modelo = modelos.buscar(id=id, contenidos_tambien=contenidos_tambien)

    return jsonify(modelo.to_dict())


@blue_print.route('', methods=['GET'])
def buscar_por_nombre():

    contenidos_tambien = request.args.get('base64') == 'true'
    nombre = request.args.get('nombre')

    modelo = modelos.buscar_por_nombre(nombre=nombre,
                                       contenidos_tambien=contenidos_tambien)

    return jsonify(modelo.to_dict())


@blue_print.route('', methods=['POST'])
def guardar():

    parametros = request.form.to_dict()

    archivos = []
    for nombre_archivo, archivo_python in request.files.to_dict().items():

        archivo = Archivo(rama=RAMA_MODELOS,
                          nombre=nombre_archivo,
                          contenido=archivo_python.read())
        archivos.append(archivo)

    modelo = Modelo(nombre=parametros['nombre'], archivos=archivos)
    id = modelos.guardar(modelo)

    respuesta = {'id': str(id), 'nombre_modelo': parametros['nombre']}

    return jsonify(respuesta), 201
