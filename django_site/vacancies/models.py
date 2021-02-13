from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Vacancies(models.Model):
    """ Таблица в бд для всех вакансий с парсинга."""

    shown_to_users = models.ManyToManyField(User, related_name='shown_vacancies')
    banned_by_users = models.ManyToManyField(User, related_name='banned_vacancies')
    id_vacancy = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    salary_from = models.CharField(max_length=100, blank=True)
    salary_to = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)
    published = models.DateTimeField(blank=True)
    contains_skills = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}, {self.area}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0),
                                 ])

    def __repr__(self):
        return self.rating
