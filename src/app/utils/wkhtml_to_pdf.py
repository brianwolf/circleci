import app.configs.variables as var
import os

from pathlib import Path
from app.configs.loggers import get_logger

DIRECTORIO_WKHTMLTOPDF = var.get('DIRECTORIO_WKHTMLTOPDF')
DIRECTORIO_RAIZ_PROYECTO = str(Path.cwd()) + '/'

logger = get_logger()


class Wkhtml_to_pdf(object):
    '''
    Objeto que representa los parametros del comando wkhtmltopdf
    '''
    def __init__(
            self,
            ruta_html: str,
            ruta_pdf: str,
            page_size: str = 'A4',
            #  disable_smart_shrinking: bool = True,
            footer_font_size: int = 8,
            zoom: float = 1):

        self.ruta_html = DIRECTORIO_RAIZ_PROYECTO + ruta_html
        self.ruta_pdf = DIRECTORIO_RAIZ_PROYECTO + ruta_pdf
        self.page_size = page_size
        # self.disable_smart_shrinking = disable_smart_shrinking
        self.footer_font_size = footer_font_size
        self.zoom = zoom

    def dict(self):
        return self.__dict__

    def _get_comando_str(self) -> str:
        '''
        crea el string del comando para ejecutar en consola
        '''
        comando = f'{DIRECTORIO_WKHTMLTOPDF} wkhtmltopdf'

        parametros_opcionales = ''
        parametros_obligatorios = ''

        for atributo, valor in self.dict().items():

            if _es_parametro_obligatorio(atributo):
                parametros_obligatorios += f' {valor}'
            else:
                parametros_opcionales += f' --{atributo} {valor}'

        parametros_opcionales = parametros_opcionales.replace('_', '-')
        return comando + parametros_opcionales + parametros_obligatorios

    def ejecutar(self) -> str:
        '''
        Convierte un html junto con sus css en un pdf, devuelve la ruta donde esta el pdf
        '''
        logger.info(
            f'Ejecutando comando de wkhtmltopdf: {self._get_comando_str()}')

        os.system(self._get_comando_str())
        return self.ruta_pdf


def _es_parametro_obligatorio(nombre_parametro: str) -> bool:
    '''
    Devuelve True si el nombre del parametro forma parte de la lista de parametros obligatorios 
    '''
    parametros_obligarios = ['ruta_html', 'ruta_pdf']
    return nombre_parametro in parametros_obligarios
