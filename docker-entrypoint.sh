python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manaage.py runserver 0.0.0.0:8000
exec gunicorn app.wsgi:application \
   --name app \
   --bind 0.0.0.0:80 \
   --workers 3 \
   --log-level=info \
   --log-file=/src/logs/gunicorn.log \
   --access-logfile=/src/logs/access.log \
   "$@"