from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    ''' Таблица для юзеров.'''
    text = 'Укажите дополнительные технологии, с которыми у вас есть опыт работы'
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
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    area = models.CharField('Выберите город поиска', max_length=100,
                            choices=city, default='Москва')
    salary = models.IntegerField('Уровень зарплаты', blank=True, default=0)
    experience = models.CharField('Опыт работы', max_length=20,
                                  choices=experience, default="Нет опыта")
    skills = models.CharField(text, max_length=100, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __repr__(self):
        return self.email


class Vacancies(models.Model):
    ''' Таблица в бд для всех вакансий с парсинга.'''
    users = models.ManyToManyField(User)
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
        return self.vacancy_id
