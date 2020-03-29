# :card_index_dividers:	CircleCI-Python-Template

> Ejemplo de proyecto Python3.8 con despliegue automatizado usando Circleci con Docker

![alt text](docs/img/python.png)
![alt text](docs/img/docker.png)
![alt text](docs/img/circleci.png)
![alt text](docs/img/heroku.png)

---

## :open_book: Documentacion adicional

* [Instalacion con Docker](docs/docker.md)
* [Instalacion con Python](docs/python.md)

---

## :tada: Uso

* La prueba mas simple para saber si la instalacion resulto es ejecutar una llamada REST de tipo GET con la url `http://localhost:5000/vivo`
* Utilizando **Postman** para realizar llamadas REST importar la coleccion de ejemplo ubicado en `postman/python-base.json`.

## :scroll: Scripts

Se dejan scripts para facilitar el manejo del proyecto, la cual contiene scripts para docker, heroku, python, etc.
Para ejecutarlos hay que pararse en la ruta raiz del proyecto y llamar el script desde ahi, ejemplo:
`./scripts/docker/build.sh`

## :package: Despliegue

La aplicacion se despliega de forma automatica utilizando *CircleCI* cada vez que se realiza un merge a la rama *master*,
para ello utiliza los scripts dentro de la carpeta `scripts/`, es decir que ejecutar los scripts manualmente es similar a lo que ejecutan las tasks dentro de los jobs del pipeline de circleci

Este despliegue consiste en:

**Docker**:

* Construir una nueva imagen de docker
* Crear un tag para la imagen con la version acortada del commit de *github*
* Subir la imagen a *docker hub*
* Actualizar la version *latest* existente en docker hub a esta ultima

**Heroku**:

* Construir una imagen de docker espificamente para *heroku*
* Subir la imagen creada al registry de heroku
* Desplegar la imagen generada

## :money_with_wings: Heroku

* Ingresar a la url https://circleci-template-heroku.herokuapp.com/ para probar la aplicacion.
* Al ingresar a la url https://circleci-template-heroku.herokuapp.com/variables se puede observar la *version* desplegada
  en el atributo del json respuesta `version`

## :earth_americas: Paginas

* [Docker Hub Python](https://hub.docker.com/_/python)
* [CircleCI](https://circleci.com/)
* [Emoticones del Readme](https://github.com/ikatyang/emoji-cheat-sheet)

## :grin: Autor

> **Brian Lobo**

* Github: [brianwolf](https://github.com/brianwolf)
* Docker Hub:  [brianwolf94](https://hub.docker.com/u/brianwolf94)
