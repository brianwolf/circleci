# -------------------------------
# PUBLIC
# -------------------------------
HEROKU_APP=${HEROKU_APP:-circleci-template-heroku}

HEROKU_EMAIL=${HEROKU_EMAIL:-brian.d.lobo@gmail.com}
HEROKU_API_KEY=${HEROKU_API_KEY:-a9320074-aa10-4e92-9bf4-2d6818bddd75}

DOCKER_NAMESPACE=${DOCKER_NAMESPACE:-brianwolf94}
DOCKER_IMAGE_NAME=${DOCKER_IMAGE_NAME:-docker_imagen}
DOCKER_TAG=${DOCKER_TAG:-local}


# -------------------------------
# PRIVATE
# -------------------------------
HEROKU_DOCKER_REGISTRY=registry.heroku.com