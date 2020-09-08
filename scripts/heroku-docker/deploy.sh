. ./scripts/heroku-docker/config.sh

echo "$HEROKU_API_KEY" | docker login --username $HEROKU_EMAIL --password-stdin $HEROKU_DOCKER_REGISTRY 

heroku create $HEROKU_APP || echo "Created $HEROKU_APP" 

heroku container:login
heroku container:push web -a $HEROKU_APP
heroku container:release web -a $HEROKU_APP