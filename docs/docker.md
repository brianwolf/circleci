# Instalacion con Docker

![alt text](../img/docker.svg)

## Construccion de la imagen local

* Ejecutar `./sctipts/docker/build.sh`

## Correr la imagen localmente

Ejecutar los siguientes scripts:

* `./sctipts/docker/run.sh`
* `./sctipts/docker/logs.sh`

Para parar la imagen correr el script:

* `./sctipts/docker/stop.sh`

## Puertos

* **5000**: api web de la aplicacion

## Volumes

* **resources/logs**: Logs de la aplicacion, todos los archivos generados tienen extension *.log*

---

[Volver al readme principal](../README.md)