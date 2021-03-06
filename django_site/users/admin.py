from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    ''' Регистрация пользователя в Django-админке.'''
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff',)
    list_filter = ('email', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email',
                           'password',
                           'area',
                           'salary',
                           'experience',
                           'skills',
                           )
                }
         ),
        ('Permissions', {'fields': ('is_staff',
                                    'is_active'
                                    )
                         }
         ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',
                        ),
            'fields': ('email',
                       'password1',
                       'password2',
                       'is_staff',
                       'area',
                       'salary',
                       'experience',
                       'skills',
                       )
            }
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
