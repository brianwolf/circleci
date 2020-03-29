FROM python:3.8-alpine

ARG TAG=local

WORKDIR /usr/src/


# VARIABLES PREDEFINIDAS
ENV VERSION=${TAG}

ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=5000
ENV PYTHON_GUNICORN_WORKERS=2
ENV PYTHON_GUNICORN_CONNECTIONS=1000
ENV PYTHON_NOMBRE_APP=app
ENV PYTHON_NOMBRE_FUNCION_APP=app


# EJECUCION
CMD gunicorn \
    -b ${PYTHON_HOST}:${PYTHON_PORT} \
    --reload \
    --workers=${PYTHON_GUNICORN_WORKERS} \
    --worker-connections=${PYTHON_GUNICORN_CONNECTIONS} \
    ${PYTHON_NOMBRE_APP}:${PYTHON_NOMBRE_FUNCION_APP}

EXPOSE ${PYTHON_PORT}


# DEPENDENCIAS
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt --upgrade pip


# CODIGO FUENTE
COPY ./src/app.py .
COPY ./src/apps ./apps