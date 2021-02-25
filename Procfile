web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
worker: cd /django_site/django_site && celery -A django_site worker -B -l INFO