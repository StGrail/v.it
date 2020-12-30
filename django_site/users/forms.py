from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
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
    class Meta:
        model = User
        fields = [
            'email',
            'area',
            'salary',
            'experience',
            'skills',
        ]

# PasswordResetForm(PasswordResetForm)
# PasswordChangeForm(SetPasswordForm):
# TODO Апдейт форму занести в эдит_профиль, перевести на русский и проверить бд.
