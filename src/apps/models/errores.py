from functools import wraps

from flask import jsonify

from apps.configs.loggers import get_logger

HTTP_STATUS_ERROR_NEGOCIO = 409


class AppException(Exception):
    '''
    Clase de error basico para manejar errores de negocio o errores dentro de la aplicacion
    que son esperados sus atributos son:

    codigo: usado para quien quiera atrapar la excepcion, se puede usar un str de la forma 'ERROR_ALTA_USUARIO'
    o un codigo numerico, la idea es que alguien pueda hacer un if con este codigo pudiendo hacer algo al respecto

    mensaje: contiene informacion extra en formato texto para una mayor informacion, esto es mas para quien use la api,
    un ejemplo puede ser: 'el usuario ya existe en la base de datos'
    '''

    def __init__(self, codigo, mensaje):
        self.codigo = codigo
        self.mensaje = mensaje

    def to_dict(self):
        return {'codigo': self.codigo, 'mensaje': self.mensaje}

    def respuesta_json(self):
        return jsonify(self.to_dict()), HTTP_STATUS_ERROR_NEGOCIO