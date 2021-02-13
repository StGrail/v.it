web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
worker: celery -A vacancies.tasks worker -B -l INFO