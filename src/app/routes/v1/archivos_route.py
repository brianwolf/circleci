from io import BytesIO

from flask import Blueprint, Response, jsonify, request, send_file

import app.services.modelos_service as modelos
import app.services.sistema_archivos_service as archivos
from app.utils.archivos import nombre_completo

blue_print = Blueprint('archivos', __name__, url_prefix='/api/v1/archivos')


@blue_print.route('/<nombre_modelo>/<rama>/<nombre_pdf>', methods=['GET'])
def obtener(nombre_modelo, rama, nombre_pdf):

    modelo = modelos.buscar_por_nombre(nombre_modelo, False)
    conteindo = archivos.obtener_contenido_por_nombre(rama, modelo.id,
                                                      nombre_pdf)

    buffer = BytesIO()
    buffer.write(conteindo)
    return send_file(BytesIO(conteindo),
                     mimetype='application/octet-stream',
                     as_attachment=True,
                     attachment_filename=nombre_pdf)
