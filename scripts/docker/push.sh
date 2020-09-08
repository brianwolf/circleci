. ./scripts/docker/config.sh

echo "$DOCKER_TOKEN" | docker login $DOCKER_REGISTRY --username $DOCKER_USER --password-stdin

printf "\n\nSubiendo imagen con TAG:$DOCKER_TAG\n"
docker push $DOCKER_REGISTRY/$DOCKER_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_TAG
