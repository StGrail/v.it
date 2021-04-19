from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
import django
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_site.settings')

app = Celery('django_site')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    'add-every-6-hours': {
        'task': 'vacancies.tasks.parse',
        'schedule': crontab(minute=0, hour=0),  # каждый день в полночь
        'args': ()
    },
}
app.conf.timezone = 'UTC'
