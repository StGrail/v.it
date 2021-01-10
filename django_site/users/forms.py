from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    ''' Форма создания пользователя.'''
    class Meta(UserCreationForm):
        model = User
        fields = [
            'email',
            'area',
            'salary',
            'experience',
            'skills',
        ]


class UserChangeForm(UserChangeForm):
    ''' Форма изменения данных пользователя.'''
    class Meta(UserChangeForm):
        model = User
        exclude = [
            'password',
            'password2'
        ]
        fields = [
            'area',
            'salary',
            'experience',
            'skills',
        ]

# PasswordResetForm(PasswordResetForm)
# PasswordChangeForm(SetPasswordForm):
