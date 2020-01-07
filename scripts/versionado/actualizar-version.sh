source ./scripts/versionado/ambiente.sh


# # OBTENER TAGS
# IFS='v' read -r -a array <<< "$(git tag | sort -V | tail -1)"


# # GENERAR SIGUIENTE TAG
# ULTIMA_VERSION_INT=${array[1]:-0}
# VERSION_FINAL="v$((ULTIMA_VERSION_INT + 1))"

# echo "Version a desplegar: $VERSION_FINAL"

# # SUBIR TAG
# git tag $VERSION_FINAL
# git push http://$GIT_USER:$GIT_TOKEN@github.com/$GIT_USER/$GIT_REPO.git --tags

# # GUARDO CONFIGURACION PARA LOS DEMAS JOBS
# echo $VERSION_FINAL >> ./BASH_ENV 


cd ./scripts/versionado/

git clone http://$GIT_USER:$GIT_TOKEN@github.com/$GIT_USER/$GIT_REPO.git repo/

cd repo/

IFS='v' read -r -a array <<< "$(git tag | sort -V | tail -1)"

ULTIMA_VERSION_INT=${array[1]:-0}
VERSION_FINAL="v$((ULTIMA_VERSION_INT + 1))"

git tag $VERSION_FINAL
git push https://$GIT_USER:$GIT_TOKEN@github.com/$GIT_USER/$GIT_REPO.git --tags

cd ../../../

rm -fr ./scripts/versionado/repo/
echo $VERSION_FINAL >> ./BASH_ENV 