python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn crud.wsgi:application --bind 0.0.0.0:$PORT