from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, UserChangeForm
from users.models import User
import requests
import json

# from ..requests_to_hh_api.get_test import get_test


def login(request):
    context = {
        'title': 'Login',  # title не работает
    }
    return render(request, 'login.html', context)


def join(request):
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
def profile(request):
    # params = {
    #     'User-Agent': 'api-test-agent',
    # }

    # def request_to_hh(experience='noExperience',
    #                skill='Python',
    #                area='Москва',
    #                salary_from=''):
    #     if skill != 'Python':
    #         params['text'] = f'Python+AND+{skill}'
    #     else:
    #         params['text'] = skill
    #     if area == 'Москва':
    #         params['area'] = 1
    #     if salary_from != '':
    #         params['only_with_salary'] = 'true'
    #         params['salary'] = f'{str(salary_from)}&from'
    #     else:
    #         salary_from = salary_from

    #     vacancy = requests.get('https://api.hh.ru/vacancies', params=params)
    #     vacancy_url = requests.utils.unquote(vacancy.url)
    #     vacancy_text = requests.get(vacancy_url).text
    #     vacancy_json = json.loads(vacancy_text)
    #     # for item in vacancy_json['items']:
    #     #     print(item['name'])
    #     #     print(item['alternate_url'])
    #     #     print(item['salary'])
    #     #     print(item['type'])
    #     print(vacancy_url)
    #     return vacancy_url

    # request_to_hh(experience=User.experience,
    #               area=User.area,
    #               salary_from=User.salary)
    context = {
        'title': 'Your profile',
        # 'vacancy_url': vacancy_url,  #  Сделать табличку в базе и туда писать вакансии
    }
    return render(request, 'profile.html', context)


@login_required  # Применяется не та форма.
def edit_profile(request):
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
        'form': edit_form,
    }
    return render(request, 'edit_profile.html', context)
