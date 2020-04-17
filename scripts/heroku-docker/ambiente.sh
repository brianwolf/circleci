export HEROKU_APP=${HEROKU_APP:-circleci-template-heroku}


# imagen de docker
export DOCKER_NOMBRE_IMAGEN=${DOCKER_NOMBRE_IMAGEN:-circleci}
export DOCKER_NAMESPACE=${DOCKER_NAMESPACE:-brianwolf94}

export CIRCLE_SHA1_SHORT=${CIRCLE_SHA1:0:7}
export DOCKER_TAG=${CIRCLE_SHA1_SHORT:-local}


# credenciales de Heroku
export HEROKU_EMAIL=${HEROKU_EMAIL:-brian.d.lobo@gmail.com}
export HEROKU_API_KEY=${HEROKU_API_KEY:-a9320074-aa10-4e92-9bf4-2d6818bddd75}
export HEROKU_REGISTRY=${HEROKU_REGISTRY:-registry.heroku.com}

export PORT=\$PORT