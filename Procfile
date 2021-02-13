web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
worker: celery --app=--pythonpath.django_site worker -B -l INFO