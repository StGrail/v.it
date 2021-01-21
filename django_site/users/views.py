from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from recommendation.recommendation_services import recommendations
from users.forms import UserCreationForm, UserChangeForm
from .models import User, Vacancies


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
def profile(request):
    ''' Профиль юзера с выводом вакансий для него.'''
    user_request = User.objects.filter(email=request.user).values('area',
                                                                  'salary',
                                                                  'experience',
                                                                  'skills',
                                                                  )
    area = user_request[0]['area']
    experience = user_request[0]['experience']
    salary = user_request[0]['salary']
    vacanies_list = Vacancies.objects.filter(area=area,
                                             experience=experience,
                                             salary_from__lte=salary,
                                             salary_to__gte=salary,
                                             ).values('name',
                                                      'url',
                                                      ).order_by('-published')
    paginator = Paginator(vacanies_list, 10)
    recommended_vacancies_id = recommendations(user_request)
    if recommended_vacancies_id:
        recommended_vacancies_to_view = Vacancies.objects.filter(id__in=recommended_vacancies_id,
                                                                 ).values('name', 'url')
    else:
        recommended_vacancies_to_view = None

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Your profile',
        'page_obj': page_obj,
        'recommended_vacancies': recommended_vacancies_to_view,
    }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    ''' Изменение данных профиля в лк.'''
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
