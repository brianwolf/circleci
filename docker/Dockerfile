# ---------------------------------------------
# COMPILER
# ---------------------------------------------
FROM python:3.8.3-slim as compiler

WORKDIR /lobezzzno
COPY ./src/logic ./src/logic
COPY ./src/app.py ./src

RUN pip install compile --upgrade pip
RUN python -m compile -b -f -o ./dist ./src


# ---------------------------------------------
# EXECUTION
# ---------------------------------------------
FROM python:3.8-alpine

ARG ARG_VERSION=local

WORKDIR /lobezzzno

# RECURSOS
COPY ./src/consume ./consume
COPY --from=compiler /lobezzzno/dist/* .


# VARIABLES PREDEFINIDAS
ENV VERSION=${ARG_VERSION}

ENV PYTHON_HOST=0.0.0.0
ENV PYTHON_PORT=80
ENV PYTHON_GUNICORN_WORKERS=1
ENV PYTHON_GUNICORN_CONNECTIONS=1000


# EJECUCION
EXPOSE ${PYTHON_PORT}

CMD gunicorn \
    -b ${PYTHON_HOST}:${PYTHON_PORT} \
    --reload \
    --workers=${PYTHON_GUNICORN_WORKERS} \
    --worker-connections=${PYTHON_GUNICORN_CONNECTIONS} \
    app:app


# DEPENDENCIAS
COPY ./src/requirements.txt . 
RUN pip install -r requirements.txt --upgrade pip
RUN rm requirements.txt