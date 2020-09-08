from enum import Enum
from typing import List

ruta_archivo: str = 'consume/config/variables.env'

no_mostrar: List[str] = ['NIVEL_LOGS']


class Variable(Enum):
    VERSION = 'VERSION'
    PYTHON_HOST = 'PYTHON_HOST'
    PYTHON_PORT = 'PYTHON_PORT'
    NIVEL_LOGS = 'NIVEL_LOGS'
    DIRECTORIO_LOGS = 'DIRECTORIO_LOGS'
    DIRECTORIO_TEMP = 'DIRECTORIO_TEMP'
