import os

from apps.configs.variables import Variable, _no_mostrar

__version__ = '1.2.0'

_RUTA_ARCHIVO_VARIABLES_PREDEFINIDAS = 'config/variables_predefinidas.env'


def dame(variable: Variable) -> str:
    '''
    Obtiene el valor de la variable de entorno correspondiente, en caso de no obtenerla, 
    la saca del diccionario de variables predefinidas
    '''
    valor_de_diccionario = _variables_predefinidas.get(variable.value)
    return os.environ.get(variable.value, valor_de_diccionario)


def variables_cargadas() -> dict:
    '''
    Devuelve el mapa de variables con sus valores instanciados y filtrados por la lista de no mostrados
    '''
    return {
        clave: dame(Variable(clave))
        for clave in Variable.__members__.keys()
        if clave not in _no_mostrar
    }


def cargar_variables_predefinidas():
    '''
    Carga el diccionario de variables predefinidas de un archivo .env
    '''
    variables = {}

    with open(_RUTA_ARCHIVO_VARIABLES_PREDEFINIDAS, 'r') as archivo:
        renglones_archivo = archivo.readlines()

    for renglon in renglones_archivo:

        if renglon.startswith('#') or renglon == '\n':
            continue

        clave, valor = renglon.split('=')

        if '#' in valor:
            valor = valor[:valor.index('#')].strip()

        variables[clave] = valor.replace('\n', '')

    return variables


_variables_predefinidas = cargar_variables_predefinidas()
