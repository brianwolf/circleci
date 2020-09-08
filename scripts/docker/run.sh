docker network create $DOCKER_NETWORK

docker run -d --rm \
--network $DOCKER_NETWORK \
--env-file $DOCKER_ENV_FILE \
--name $DOCKER_IMAGE_NAME \
-p 80:80 \
$DOCKER_USER/$DOCKER_IMAGE_NAME:$DOCKER_TAG
