from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, UserChangeForm
from .models import User, Vacancies
from hh_parser.vacancy_to_db import input_request, search_and_save


def join(request):
    ''' Регистрации юзера с последующим редиректом на страницу логина.'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы были успешно зарегистрированы.')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {
        'title': 'Join',
        'form': form,
    }
    return render(request, 'join.html', context)


@login_required
def profile(request):  # Обработать вывод, если нет данных
    ''' Профиль юзера с выводом вакансий для него.'''
    try:
        query_set = User.objects.filter(email=request.user).values('salary',
                                                                   'area',
                                                                   'experience',
                                                                    )[0]
        user_request = {
            'salary_from': query_set['salary'],
            'area': query_set['area'],
            'experience': query_set['experience'],
        }
        # find_vacancy = input_request(**user_request)
        # vacancies = search_and_save(request, find_vacancy)
        """Достать и добавить вакансии из бд"""
        text = 'Скоро тут будет список вакансий для Вас!'  # Заменить на данные из бд.
        context = {
            'title': 'Your profile',
            'text': text,
        }
        return render(request, 'profile.html', context)
    except KeyError:
        text = 'Завершите регистрацию.'
        context = {
            'title': 'Your profile',
            'text': text,
        }
        return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    ''' Изменениеданных профиля в лк.'''
    if request.method == 'POST':
        edit_form = UserChangeForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,
                             'Ваши данные были успешно изменены.')
            return redirect('profile')
    else:
        edit_form = UserChangeForm(instance=request.user)

    context = {
        'title': 'Edit',
        'edit_form': edit_form,
    }
    return render(request, 'edit_profile.html', context)
