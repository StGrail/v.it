web: gunicorn --pythonpath django_site core.wsgi --log-file -
worker: sh -c 'cd django_site && python3 manage.py parser'