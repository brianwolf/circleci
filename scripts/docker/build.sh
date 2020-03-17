source ./scripts/docker/ambiente.sh

echo $DOCKER_TAG

docker build \
--build-arg TAG=$DOCKER_TAG \
$(for i in `cat $DOCKER_ARCHIVO_ARGUMENTOS`; do out+="--build-arg $i " ; done; echo $out;out="") \
-f $DOCKER_DOCKERFILE \
-t $DOCKER_USER/$DOCKER_NOMBRE_IMAGEN:$DOCKER_TAG . \
--no-cache
