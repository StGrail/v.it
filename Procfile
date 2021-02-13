web: gunicorn --pythonpath django_site django_site.wsgi --log-file -
worker: celery -A django_site.vacancies.tasks worker -l INFO