source ./scripts/actualizar-config/ambiente.sh


# SE BORRA LA CARPETA EN CASO DE QUE YA EXISTA
rm -fr $GIT_CARPETA_DESCARGA


# SE CLONA EL REPO
git clone https://$GIT_USER:$GIT_TOKEN@github.com/$GIT_USER/$GIT_REPO.git \
-b ${CIRCLE_BRANCH:-master} \
$GIT_CARPETA_DESCARGA


# SE REEMPLAZAN LOS ARCHIVOS DE CONFIGURACION
cp -fa $GIT_CARPETA_DESCARGA/ambiente.env ./config
cp -fa $GIT_CARPETA_DESCARGA/argumentos.env ./config