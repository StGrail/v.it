from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import forms
from .models import User, Blabla


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = (
            'email',
            )


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email',)


class FullReg(forms.ModelForm):
    class Meta:
        model = Blabla
        fields = [
            'area',
            'salary',
            'experience',
            'skills',
        ]


class UpdateReg(forms.ModelForm):
    class Meta:
        model = Blabla
        fields = [
            'area',
            'salary',
            'experience',
            'skills',
        ]
# TODO Апдейт форму занести в эдит_профиль, перевести на русский и проверить бд.
