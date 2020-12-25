from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    EXPERIENCE = [
        ("noExperience", "Нет опыта"),
        ("between1And3", "От 1 года до 3 лет"),
        ("between3And6", "От 3 до 6 лет"),
        ("moreThan6", "Более 6 лет")
    ]

    AREA = [
        ('1', 'Москва'),
        ('2', 'Санкт-Петербург'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    зарплата = models.PositiveIntegerField(default=0)
    город = models.CharField(max_length=100, choices=AREA, default='1')
    опыт = models.CharField(max_length=100, choices=EXPERIENCE,
                            default="noExperience")
    skills = models.CharField(max_length=30)

    def __repr__(self):
        return f'{self.user.username} Profile'
