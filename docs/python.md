# Instalacion con Python 3.8

> Para esto **se toma como directorio raiz** la carpeta `src/` por lo que todos los
comandos mostrados se ejecutan dentro de esta carpeta

![alt text](../img/python.png)

## Ambiente virtual

* Con *virtualenv* instalado ejecutar: `virtualenv -p python3.8 env`
* Entrar en la virtual env con `source env/bin/activate`
* Instalar los requerimientos con `pip install -r requirements.txt`

Para salir de la virtual env ejecutar `deactivate`

## Correr con Flask

Dentro del ambiente virtual creado ejecutar: `python app.py`

## Puertos

* **5000**: api web de la aplicacion

## Carpetas generadas

* **resources/logs**: Logs de la aplicacion, todos los archivos generados tienen extension *.log*

---

[Volver al readme principal](../README.md)