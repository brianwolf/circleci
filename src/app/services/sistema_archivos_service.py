import os
import app.configs.variables as var
import app.utils.archivos as util_archivos

from uuid import UUID
from app.configs.loggers import get_logger
from app.models.errores import ErrorApp
from app.models.modelos import Archivo

CARPETA_SISTEMA_ARCHIVOS = var.get('CARPETA_SISTEMA_ARCHIVOS')


def guardar_archivo(uuid: UUID, archivo: Archivo):
    '''
    Crea el arachivo en el sistema de archivos, la estructura que maneja
    es:

    {rama}/{uuid}/{archivo.nombre}

    IMPORTANTE: el nombre debe incluir la extension del archivo
    '''
    try:
        directorio = ruta_modelo(archivo.rama, uuid)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        ruta = ruta_completa(archivo.rama, uuid, archivo.nombre)

        with open(ruta, 'wb+') as archivo_python:
            archivo_python.write(archivo.contenido)

    except IOError as e:
        get_logger().error(str(e))

        mensaje = f'El archivo ubicado en {ruta_completa} NO se pudo guardar'
        raise ErrorApp('ARCHIVO_NO_GUARDADO', mensaje)


def obtener_contenido_por_nombre(rama: str, uuid: UUID, nombre: str) -> bytes:
    '''
    Devuelve el contenido del archivo
    '''
    ruta = ruta_completa(rama, uuid, nombre)
    try:
        with open(ruta, 'rb') as archivo:
            contenido = archivo.read()

        return contenido

    except IOError as e:
        get_logger().error(str(e))

        mensaje = f'El archivo ubicado en {ruta} NO fue encontrado'
        raise ErrorApp('ARCHIVO_NO_ENCONTRADO', mensaje)


def obtener_contenido(ruta: str) -> bytes:
    '''
    Devuelve el contenido del archivo por su ruta completa
    '''
    try:
        with open(ruta, 'rb') as archivo:
            contenido = archivo.read()

        return contenido

    except IOError as e:
        get_logger().error(str(e))

        mensaje = f'El archivo ubicado en {ruta} NO fue encontrado'
        raise ErrorApp('ARCHIVO_NO_ENCONTRADO', mensaje)


def listado_archivos(rama: str, uuid: UUID) -> list:
    '''
    Devuelve un listado de los nombres de los archivos pertenecientes a usa uuid
    '''
    ruta = ruta_modelo(rama, uuid)
    try:
        return os.listdir(ruta)

    except IOError:
        mensaje = f'La uuid {uuid} NO fue encontrada'
        get_logger().error(mensaje)

        raise ErrorApp('UUID_NO_ENCONTRADA', mensaje)


def borrar_archivo(rama: str, uuid: UUID, nombre: str):
    '''
    Elimina el archivo del sistema de archivos
    '''
    ruta = ruta_completa(rama, uuid, nombre)
    try:
        os.remove(ruta)

    except IOError as e:
        get_logger().error(str(e))

        mensaje = f'El archivo ubicado en {ruta} NO fue encontrado'
        raise ErrorApp('ARCHIVO_NO_ENCONTRADO', mensaje)


def borrar_carpeta_y_archivos(rama: str, uuid: UUID):
    '''
    Elimina la carpeta con todos sus archivos
    '''
    ruta = ruta_modelo(rama, uuid)
    try:
        os.remove(ruta)

    except IOError as e:
        get_logger().error(str(e))

        mensaje = f'El archivo ubicado en {ruta} NO fue encontrado'
        raise ErrorApp('ARCHIVO_NO_ENCONTRADO', mensaje)


def ruta_completa(rama: str, uuid: UUID, nombre: str) -> str:
    '''
    Devuelve la ruta completa del archivo
    '''
    return f'{ruta_modelo(rama, uuid)}{nombre}'


def ruta_modelo(rama: str, uuid: UUID) -> str:
    '''
    Devuelve la ruta completa del archivo
    '''
    return f'{CARPETA_SISTEMA_ARCHIVOS}/{rama}/{uuid}/'
