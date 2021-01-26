from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ''' Таблица для юзеров.'''
    additional_skills = 'Через зарятую укажите дополнительные технологии, '
    additional_skills += 'с которыми у вас есть опыт работы.'
    text = 'Многие работодатели не указывают уровень зп, показывать такие вакансии?'
    city = (
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
    )
    experience = (
        ("нет опыта", "Нет опыта"),
        ("от 1 года до 3 лет", "От 1 года до 3 лет"),
        ("от 3 до 6 лет", "От 3 до 6 лет"),
        ("более 6 лет", "Более 6 лет"),
    )
    show_without_salary = (
        (False, 'Не показывать'),
        (True, 'Показывать'),
    )
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    area = models.CharField('Выберите город поиска', max_length=100,
                            choices=city, default='Москва')
    salary = models.IntegerField('Уровень зарплаты', blank=True, default=0)
    without_salary = models.BooleanField(text, choices=show_without_salary,
                                         default=False)
    experience = models.CharField('Опыт работы', max_length=20,
                                  choices=experience, default="Нет опыта")
    skills = models.CharField(additional_skills, max_length=100, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __repr__(self):
        return self.email


class Vacancies(models.Model):
    ''' Таблица в бд для всех вакансий с парсинга.'''
    shown_to_users = models.ManyToManyField(User)
    id_vacancy = models.CharField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    experience = models.CharField(max_length=100, blank=True)
    salary_from = models.CharField(max_length=100, blank=True)
    salary_to = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100, blank=True)
    published = models.DateTimeField(blank=True)
    contains_skills = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label = 'users'
        managed = True

    def __repr__(self):
        return self.id_vacancy


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0),
                                 ]
                                 )

    def __str__(self):
        return str(self.pk)
