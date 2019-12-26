import app.configs.variables as var
import app.services.modelos_service as modelos_service
import app.services.sistema_archivos_service as archi
import uuid
import os

from app.configs.loggers import get_logger
from app.models.modelos import Modelo, Archivo
from jinja2 import Template
from app.utils.wkhtml_to_pdf import Wkhtml_to_pdf
from app.models.conversores import HtmlToPdf

RAMA_MODELOS = var.get('RAMA_MODELOS')
RAMA_PDFS = var.get('RAMA_PDFS')


def html_to_pdf(modelo: Modelo, htmlToPdf: HtmlToPdf, nombre_html: str,
                nombre_pdf: str) -> str:
    '''
    Genera un reporte en pdf aplicando los datos al modelo
    Devuelve la ruta interna de donde guardo el archivo
    '''
    cotenido_str = modelo.contenido_html(nombre_html).decode()
    template_renderizado = Template(cotenido_str).render(htmlToPdf.datos)

    nombre_html_temporal = str(uuid.uuid4()) + '.html'
    html_temporal = Archivo(rama=RAMA_MODELOS,
                            nombre=nombre_html_temporal,
                            contenido=bytes(template_renderizado, 'utf-8'))
    archi.guardar_archivo(modelo.id, html_temporal)

    directorio_modelo = archi.ruta_modelo(RAMA_MODELOS, modelo.id)
    ruta_html_temporal = directorio_modelo + html_temporal.nombre

    directorio_pdf = archi.ruta_modelo(RAMA_PDFS, modelo.id)
    ruta_pdf = directorio_pdf + nombre_pdf
    if not os.path.exists(directorio_pdf):
        os.makedirs(directorio_pdf)

    htmlToPdf.config.ruta_html = ruta_html_temporal
    htmlToPdf.config.ruta_pdf = ruta_pdf
    htmlToPdf.config.ejecutar()

    archi.borrar_archivo(RAMA_MODELOS, modelo.id, nombre_html_temporal)

    return ruta_pdf
