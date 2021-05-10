from celery import shared_task
import celery
import time
from django.core.management import call_command


@shared_task
def parse():
    try:
        print('celery worker')
        call_command("parser")
        return "success"
    except:
        print("error")
