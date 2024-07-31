poetry new my-folder --src --name package1

python src

poetry build

poetry install

poetry run mycli

poetry run python src

poetry run pytest tests

# Build production docker container
docker build -f ../dockerfiles/Dockerfile.prod -t mytest:prod .

docker run --rm mytest:prod
