web: gunicorn organizer_fine_api.wsgi.py
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput