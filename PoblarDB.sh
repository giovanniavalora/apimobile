#!/bin/sh

# ./apimobile/LimpiarBDyMigraciones.sh
cd /Users/nreyesgradiente/Desktop/Avalora/Camiones/docker

docker-compose -f "docker-compose.yml" exec apimob 
docker-compose -f "docker-compose.yml" exec db psql --username=ohl --dbname=ohlcamiones

# docker-compose -f "docker-compose.prod.yml" exec db psql --username=ohl --dbname=ohlcamiones_prod
exec "$@"
