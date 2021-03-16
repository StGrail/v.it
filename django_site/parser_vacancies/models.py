from django.db import models

from vacancies.models import Vacancies


class Skills(models.Model):
    id_vacancy = models.OneToOneField(Vacancies, on_delete=models.CASCADE)
    sql = models.BooleanField(default=False)
    linux = models.BooleanField(default=False)
    git = models.BooleanField(default=False)
    postgresql = models.BooleanField(default=False)
    django = models.BooleanField(default=False)
    flask = models.BooleanField(default=False)
    css = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    bash = models.BooleanField(default=False)
    mysql = models.BooleanField(default=False)
    oop = models.BooleanField(default=False)
    docker = models.BooleanField(default=False)
    mongodb = models.BooleanField(default=False)
    pandas = models.BooleanField(default=False)
    numpy = models.BooleanField(default=False)
    jira = models.BooleanField(default=False)
    kubernetes = models.BooleanField(default=False)
    http = models.BooleanField(default=False)
    tcp_ip = models.BooleanField(default=False)
    trello = models.BooleanField(default=False)
    unix = models.BooleanField(default=False)
    redis = models.BooleanField(default=False)

    def __repr__(self):
        return self.id_vacancy

    
class Vacancies_count(models.Model):
    date = models.DateField(unique=True, null=True, auto_now=True)
    added_today = models.IntegerField(null=True)
    total_vacancies_count = models.IntegerField(null=True)

    def __repr__(self):
        return f'{self.date} added {self.added_today} vacancies'
