web: gunicorn --pythonpath django_site core.wsgi --log-file -
worker: sh -c 'cd ./django_site/ && celery -A django_site worker -B -l INFO'