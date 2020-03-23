# CIRCLECI

> Ejemplo de arquitectura de un proyecto usando **python3.8**, **circleci** y **docker**

![alt text](img/python.png)
![alt text](img/circleci.png)
![alt text](img/docker.svg)

---

## Indice

* [Instalacion con Docker](docs/docker.md)
* [Instalacion con Python](docs/python.md)
* [Uso](#uso)
* [Scripts](#scripts)
* [Despliegue Automatizado](#despliegue)
* [Paginas](#paginas)
* [Autor](#autor)

---

## Uso

* La prueba mas simple para saber si la instalacion resulto es ejecutar una llamada REST de tipo GET con la url `http://localhost:5000/vivo`
* Utilizando **Postman** para realizar llamadas REST importar la coleccion de ejemplo ubicado en `postman/python-base.json`.

## Scripts

Se dejan scripts para facilitar el manejo del proyecto, la cual contiene scripts para docker, heroku, python, etc.
Para ejecutarlos hay que pararse en la ruta raiz del proyecto y llamar el script desde ahi, ejemplo:
`./scripts/docker/build.sh`

## Despliegue

La aplicacion se despliega de forma automatica utilizando *CircleCi* cada vez que se realiza un merge a la rama *master*,
para ello utiliza los scripts dentro de la carpeta `scripts/`, es decir que ejecutar los scripts manualmente es similar a lo que ejecutan las tasks dentro de los jobs del pipeline de circleci

## Paginas

* [Docker Hub Python](https://hub.docker.com/_/python)
* [CircleCI](https://circleci.com/)

## Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
