source ./scripts/heroku/ambiente.sh
source ./scripts/docker/ambiente.sh

cd ./scripts/heroku

# echo $(heroku auth:token) | docker login -u $USER --password-stdin registry.heroku.com
echo "$DOCKER_TOKEN" | docker login --username $DOCKER_USER --password-stdin registry.heroku.com

heroku container:login
heroku container:push web -a $HEROKU_APP --arg TAG=$DOCKER_TAG
heroku container:release web -a $HEROKU_APP

cd ../../
