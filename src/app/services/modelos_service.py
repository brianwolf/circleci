import app.configs.variables as var
import app.repositories.modelos_repository as repo
import app.services.sistema_archivos_service as archi

from app.models.modelos import Modelo, ModeloDocument, Archivo, ArchivoDocument
from app.models.errores import ErrorApp
from app.utils.wkhtml_to_pdf import Wkhtml_to_pdf
from app.configs.loggers import get_logger
from uuid import UUID


def guardar(modelo: Modelo) -> UUID:
    '''
    Guarda un modelo en la base de datos y en el sistema de archivos
    '''
    id_generada = repo.guardar(ModeloDocument.por_modelo(modelo))
    try:
        for archivo in modelo.archivos:
            archi.guardar_archivo(uuid=id_generada, archivo=archivo)

    except ErrorApp as ae:
        archi.borrar_carpeta_y_archivos(id_generada)
        repo.borar_por_id(id_generada)
        raise ae

    return id_generada


def borrar_por_nombre(nombre: str):
    '''
    Borra un modelo en la base de datos y en el sistema de archivos buscando por nombre
    '''
    modelo = repo.buscar_por_nombre(nombre)
    if not modelo:
        mensaje = f'No se encuentro el modelo de nombre {nombre}'
        raise ErrorApp('MODELO_NO_ENCONTRADO', mensaje)

    archi.borrar_carpeta_y_archivos(modelo.id)
    repo.borar_por_id(modelo.id)


def borrar(id: UUID):
    '''
    Borra un modelo en la base de datos y en el sistema de archivos
    '''
    archi.borrar_carpeta_y_archivos(id)
    repo.borar_por_id(id)


def buscar(id: UUID, contenidos_tambien: bool = False) -> Modelo:
    '''
    Busca un modelo en la base de datos y en el sistema de archivos
    '''
    modelo_document = repo.buscar_por_id(id)
    archivos = _obtener_archivos(modelo_document, contenidos_tambien)

    modelo = Modelo(nombre=modelo_document.nombre,
                    id=modelo_document.id,
                    fecha_creacion=modelo_document.fecha_creacion,
                    archivos=archivos)

    return modelo


def buscar_por_nombre(nombre: str, contenidos_tambien: bool = False) -> Modelo:
    '''
    Busca un modelo en la base de datos y en el sistema de archivos
    '''
    modelo_document = repo.buscar_por_nombre(nombre)
    archivos = _obtener_archivos(modelo_document, contenidos_tambien)

    modelo = Modelo(nombre=modelo_document.nombre,
                    id=modelo_document.id,
                    fecha_creacion=modelo_document.fecha_creacion,
                    archivos=archivos)

    return modelo


def _obtener_archivos(modelo_document: ModeloDocument,
                      contenidos_tambien: bool = False):

    archivos = []
    for archivo_document in modelo_document.archivos:

        archivo = Archivo(rama=archivo_document.rama,
                          nombre=archivo_document.nombre,
                          contenido=None,
                          fecha_creacion=archivo_document.fecha_creacion)

        if contenidos_tambien:
            contenido = archi.obtener_contenido_por_nombre(
                rama=archivo_document.rama,
                uuid=modelo_document.id,
                nombre=archivo_document.nombre)

            archivo.contenido = contenido

        archivos.append(archivo)

    return archivos