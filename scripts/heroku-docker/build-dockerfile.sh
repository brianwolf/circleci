. ./scripts/heroku-docker/config.sh

echo "FROM $HEROKU_DOCKER_NAMESPACE/$HEROKU_DOCKER_IMAGE_NAME:$HEROKU_DOCKER_TAG" > Dockerfile