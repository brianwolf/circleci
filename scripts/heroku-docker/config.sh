# -------------------------------
# PUBLIC
# -------------------------------
export HEROKU_APP=${HEROKU_APP:-circleci-template-heroku}

export HEROKU_EMAIL=${HEROKU_EMAIL:-brian.d.lobo@gmail.com}
export HEROKU_API_KEY=${HEROKU_API_KEY:-a9320074-aa10-4e92-9bf4-2d6818bddd75}

export DOCKER_NAMESPACE=${DOCKER_NAMESPACE:-brianwolf94}
export DOCKER_IMAGE_NAME=${DOCKER_IMAGE_NAME:-docker_imagen}
export DOCKER_TAG=${DOCKER_TAG:-local}


# -------------------------------
# PRIVATE
# -------------------------------
export HEROKU_DOCKER_REGISTRY=registry.heroku.com