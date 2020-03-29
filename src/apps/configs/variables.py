from enum import Enum


class Variable(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    NIVEL_LOGS = 'NIVEL_LOGS'
    DIRECTORIO_LOGS = 'DIRECTORIO_LOGS'
    NOMBRE_LOG_PREDEFINIDO = 'NOMBRE_LOG_PREDEFINIDO'
    NO_MOSTRAR_EJEMPLO = 'NO_MOSTRAR_EJEMPLO'


_predefinidas = {
    'VERSION': 'local',
    'PYTHON_HOST': 'localhost',
    'PYTHON_PORT': 5000,
    'NIVEL_LOGS': 'INFO',
    'DIRECTORIO_LOGS': 'resources/logs/',
    'NOMBRE_LOG_PREDEFINIDO': 'app',
    'NO_MOSTRAR_EJEMPLO': 'soy_un_secreto'
}

_no_mostrar = ['NO_MOSTRAR_EJEMPLO']
