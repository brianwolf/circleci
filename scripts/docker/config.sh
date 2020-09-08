# -------------------------
# PUBLIC
# -------------------------

export DOCKER_USER=${DOCKER_USER:-brianwolf94}
export DOCKER_TOKEN=${DOCKER_TOKEN:-64f0e37f-eb5a-4072-8b5b-a1a2b7e7b7cf}

export DOCKER_REGISTRY=${DOCKER_REGISTRY:-docker.io}
export DOCKER_NAMESPACE=${DOCKER_NAMESPACE:-brianwolf94}
export DOCKER_IMAGE_NAME=${DOCKER_IMAGE_NAME:-docker_imagen}
export DOCKER_TAG=${DOCKER_TAG:-local}


# -------------------------
# PRIVATE
# -------------------------

export DOCKER_ARG_FILE=./docker/config/argumentos.env
export DOCKER_ENV_FILE=./docker/config/ambiente.env
export DOCKER_DOCKERFILE=./docker/Dockerfile

export DOCKER_NETWORK=docker-red

# CIRCLE_SHA1_SHORT=${CIRCLE_SHA1:0:7}
# DOCKER_TAG=${CIRCLE_SHA1_SHORT:-local}
