cd /home/ohl/controlCamionesApi/apimobile
git checkout develop
git pull
cd /home/ohl/controlCamionesApi/
docker-compose -f docker-compose.prod.yml stop web
docker-compose -f docker-compose.prod.yml build web
docker-compose -f docker-compose.prod.yml up -d web
# docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
# docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
# docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
