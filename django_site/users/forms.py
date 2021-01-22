from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm

from .models import User, Vacancies


class UserCreationForm(UserCreationForm):
    ''' Форма создания пользователя.'''
    class Meta(UserCreationForm):
        model = User
        fields = [
            'email',
            'area',
            'salary',
            'without_salary',
            'experience',
            'skills',
        ]


class UserChangeForm(ModelForm):
    ''' Форма изменения данных пользователя.'''
    class Meta(UserChangeForm):
        model = User
        fields = [
            'area',
            'salary',
            'experience',
            'without_salary',
            'skills',
        ]


class Rating(forms.Form):
    CHOISES = (
        (0, 'Больше не показывать'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = forms.ChoiceField(label='Оцените вакансию:',
                               choices=CHOISES,
                               required=False,
                               )
