import os
from app.configs.mapa_variables import mapa_variables

RUTA_ARCHIVO_PREDEFINIDO = 'app/configs/predefinido.properties'


def get(variable: str):
    '''
    Obtiene el valor de la variable de entorno correspondiente, en caso de no obtenerla, 
    la saca del archivo de configuracion
    '''
    valor_de_diccionario = mapa_variables[variable]
    return os.environ.get(variable, valor_de_diccionario)


def _get_diccionario_de_archivo_predefinido() -> dict:
    '''
    Crea un diccionario en base al archivo de configuracion de .env
    '''
    archivo = open(RUTA_ARCHIVO_PREDEFINIDO, 'r').read()
    lista_clave_valor = archivo.split('\n')

    diccionario = {}
    for clave_valor in lista_clave_valor:

        if '=' in clave_valor and not clave_valor.startswith("#"):
            clave = clave_valor.split('=')[0].strip()
            valor = clave_valor.split('=')[1].strip()

            diccionario[clave] = valor

    return diccionario
