web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
celeryworker: celery worker --app=django_site --loglevel=info