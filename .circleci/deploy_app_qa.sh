cd /home/ohl/controlCamionesApi/apimobile
git checkout develop
git pull https://github.com/giovanniavalora/apimobile.git develop
cd /home/ohl/controlCamionesApi/
# docker-compose -f docker-compose.prod.yml up -d --build
#docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
#docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
#docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
