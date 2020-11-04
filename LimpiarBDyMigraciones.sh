#!/bin/sh

# ./apimobile/LimpiarBDyMigraciones.sh
cd /Users/nreyesgradiente/Desktop/Avalora/Camiones/docker

docker-compose -f "docker-compose.yml" exec apimob rm -rf api/migrations
docker-compose -f "docker-compose.yml" down
docker volume rm docker_postgres_data
docker-compose -f "docker-compose.yml" up -d
# docker-compose -f "docker-compose.yml" exec apimob python manage.py migrate --fake
docker-compose -f "docker-compose.yml" exec apimob python manage.py makemigrations api
# docker-compose -f "docker-compose.yml" exec apimob python manage.py migrate --fake-initial
docker-compose -f "docker-compose.yml" exec apimob python manage.py migrate

# docker-compose -f "docker-compose.yml" exec db psql --username=ohl --dbname=ohlcamiones


###Para DigitalOcean:
# docker-compose -f "docker-compose.prod.yml" exec web rm -rf api/migrations
# docker-compose -f "docker-compose.prod.yml" down
# docker volume rm docker_postgres_data
# docker-compose -f "docker-compose.prod.yml" up -d
# # docker-compose -f "docker-compose.yml" exec apimob python manage.py migrate --fake
# docker-compose -f "docker-compose.prod.yml" exec web python manage.py makemigrations api
# # docker-compose -f "docker-compose.yml" exec apimob python manage.py migrate --fake-initial
# docker-compose -f "docker-compose.prod.yml" exec web python manage.py migrate
# # docker-compose -f "docker-compose.prod.yml" exec db psql --username=ohl --dbname=ohlcamiones_prod
exec "$@"
