release: python manage.py migrate
web: gunicorn example.wsgi --bind=0.0.0.0:$PORT
