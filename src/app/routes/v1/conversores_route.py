import json
import os
import io
import app.services.conversores_service as conversores
import app.services.sistema_archivos_service as archivos
import app.services.modelos_service as modelos_service
import app.configs.variables as var

from app.utils.wkhtml_to_pdf import Wkhtml_to_pdf
from app.models.conversores import HtmlToPdf
from datetime import datetime
from flask import jsonify, Blueprint, request, send_file, Response
from werkzeug import FileWrapper
from io import BytesIO
from app.utils.archivos import nombre_completo

blue_print = Blueprint('reportes', __name__, url_prefix='/api/v1/reportes')


@blue_print.route('/<nombre_modelo>/html/<nombre_html>/pdf/<nombre_pdf>',
                  methods=['POST'])
def html_to_pdf(nombre_modelo, nombre_html, nombre_pdf):

    json_body = request.json
    json_body['config']['ruta_html'] = ''
    json_body['config']['ruta_pdf'] = ''

    wkhtml_to_pdf = Wkhtml_to_pdf(**json_body['config'])
    htmlToPdf = HtmlToPdf(wkhtml_to_pdf, json_body['datos'])

    nombre_html = nombre_completo(nombre_html, 'html')
    nombre_pdf = nombre_completo(nombre_pdf, 'pdf')

    modelo = modelos_service.buscar_por_nombre(nombre_modelo, True)
    ruta_pdf = conversores.html_to_pdf(modelo, htmlToPdf, nombre_html,
                                       nombre_pdf)

    respuesta = {'pdf_guardado_en': ruta_pdf}
    return jsonify(respuesta), 201
