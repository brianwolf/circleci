. ./scripts/python/ambiente.sh

# INSTALAR DEPENDENCIAS
. $CARPETA_ENV/bin/activate
pip install -r $CARPETA_REQUIREMENTS


# ACTUALIZAR REQUIREMENTS
pip freeze > $CARPETA_REQUIREMENTS


# SALIR DEL VIRTUAL ENV
deactivate