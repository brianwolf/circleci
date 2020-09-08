# -------------------------
# PUBLIC
# -------------------------

DOCKER_USER=${DOCKER_USER:-brianwolf94}
DOCKER_TOKEN=${DOCKER_TOKEN:-64f0e37f-eb5a-4072-8b5b-a1a2b7e7b7cf}

DOCKER_REGISTRY=${DOCKER_REGISTRY:-docker.io}
DOCKER_NAMESPACE=${DOCKER_NAMESPACE:-brianwolf94}
DOCKER_IMAGE_NAME=${DOCKER_IMAGE_NAME:-docker_imagen}
DOCKER_TAG=${DOCKER_TAG:-local}


# -------------------------
# PRIVATE
# -------------------------

DOCKER_ARG_FILE=./docker/config/argumentos.env
DOCKER_ENV_FILE=./docker/config/ambiente.env
DOCKER_DOCKERFILE=./docker/Dockerfile

DOCKER_NETWORK=docker-red

# CIRCLE_SHA1_SHORT=${CIRCLE_SHA1:0:7}
# DOCKER_TAG=${CIRCLE_SHA1_SHORT:-local}
