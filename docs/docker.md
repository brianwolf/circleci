# :whale: Instalacion con Docker :whale:

![alt text](../img/docker.svg)

## Construcción de la imagen local

* Ejecutar `./sctipts/docker/build.sh`

## Correr la imagen local

Ejecutar los siguientes scripts:

* `./sctipts/docker/run.sh`
* `./sctipts/docker/logs.sh`

Para parar la imagen correr el script:

* `./sctipts/docker/stop.sh`

## Puertos

* **5000**: api web de la aplicación

## Volumes

* **resources/logs**: Logs de la aplicación, todos los archivos generados tienen extensión *.log*

---

[Volver al readme principal](../README.md)


