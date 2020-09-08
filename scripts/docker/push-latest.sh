. ./scripts/docker/config.sh

docker tag \
$DOCKER_REGISTRY/$DOCKER_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_TAG \
$DOCKER_REGISTRY/$DOCKER_NAMESPACE/$DOCKER_IMAGE_NAME:latest

printf "\n\nSubiendo imagen con TAG:latest\n"
docker push $DOCKER_REGISTRY/$DOCKER_NAMESPACE/$DOCKER_IMAGE_NAME:latest