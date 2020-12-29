from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    city = (
        ('Москва', 'Москва'),
        ('Санкт-Петербург', 'Санкт-Петербург'),
    )
    experience = (
        ("noExperience", "Нет опыта"),
        ("between1And3", "От 1 года до 3 лет"),
        ("between3And6", "От 3 до 6 лет"),
        ("moreThan6", "Более 6 лет"),
    )
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    area = models.CharField('город', max_length=100, choices=city,
                            default='Москва')
    salary = models.IntegerField('уровень зарплаты', null=True)
    experience = models.CharField('опыт работы', max_length=20,
                                  choices=experience, default="Нет опыта")
    text = 'укажите дополнительные технологии, с которыми у вас есть опыт'
    skills = models.CharField(text, max_length=100, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __repr__(self):
        return self.email


'''сделать связи между табличками  и зарегистировать в админ'''
