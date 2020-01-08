source ./scripts/docker/ambiente.sh

echo "$DOCKER_TOKEN" | docker login --username $DOCKER_USER --password-stdin

docker push $DOCKER_USER/$DOCKER_NOMBRE_IMAGEN:$DOCKER_TAG

docker tag $DOCKER_USER/$DOCKER_NOMBRE_IMAGEN:latest $DOCKER_USER/$DOCKER_NOMBRE_IMAGEN:$DOCKER_TAG
docker push $DOCKER_USER/$DOCKER_NOMBRE_IMAGEN:latest