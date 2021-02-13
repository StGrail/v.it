web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
worker: celery -A django_site worker -B -l INFO