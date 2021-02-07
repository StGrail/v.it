from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Таблица для юзеров."""

    additional_skills = 'Через запятую укажите дополнительные технологии, '
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



