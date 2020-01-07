source ./scripts/versionado/ambiente.sh

# a=2


# echo "$(($a + 1))"

echo $(git tag)

IFS='v' read -r -a array <<< "$(git tag)"

echo ${array[2]}