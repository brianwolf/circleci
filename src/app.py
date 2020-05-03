from flask import Flask

from apps.configs.lector_variables import cargar_variables_predefinidas, dame
from apps.configs.rest.blue_prints import carga_dinamica_de_bps
from apps.configs.rest.error_handlers import error_handler_bp
from apps.configs.rest.json import JSONEncoderPersonalizado
from apps.configs.variables import Variable

_PYTHON_HOST = dame(Variable.PYTHON_HOST)
_PYTHON_PORT = int(dame(Variable.PYTHON_PORT))

app = Flask(__name__)
app.register_blueprint(error_handler_bp)
app.json_encoder = JSONEncoderPersonalizado

carga_dinamica_de_bps(app, 'apps/routes')


if __name__ == "__main__":
    app.run(host=_PYTHON_HOST, port=_PYTHON_PORT, debug=True)
