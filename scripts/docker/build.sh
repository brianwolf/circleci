. ./scripts/docker/config.sh

docker build \
--build-arg TAG=$DOCKER_TAG \
$(for i in `cat $DOCKER_ARG_FILE`; do out+="--build-arg $i " ; done; echo $out;out="") \
-f $DOCKER_DOCKERFILE \
-t $DOCKER_NAMESPACE/$DOCKER_IMAGE_NAME:$DOCKER_TAG .