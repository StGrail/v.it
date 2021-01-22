from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from recommendation.recommendation_services import recommendations
from users.forms import UserCreationForm, UserChangeForm, Rating
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
    user_request = User.objects.filter(email=request.user).values('id',
                                                                  'area',
                                                                  'salary',
                                                                  'experience',
                                                                  'skills',
                                                                  'without_salary',
                                                                  )
    user_id = user_request[0]['id']
    area = user_request[0]['area']
    experience = user_request[0]['experience']
    salary = user_request[0]['salary']
    without_salary = user_request[0]['without_salary']
    if without_salary is False:
        vacanies_list = Vacancies.objects.filter(area=area,
                                                 experience=experience,
                                                 salary_from__lte=salary,
                                                 salary_to__gte=salary,
                                                 ).values('name',
                                                          'url',
                                                          'rating',
                                                          'id',
                                                          ).order_by('-published')
    else:
        vacanies_list = Vacancies.objects.filter(area=area,
                                                 experience=experience,
                                                 ).values('name',
                                                          'url',
                                                          'id',
                                                          ).order_by('-published')

    recommended_vacancies_id = recommendations(user_request)
    if recommended_vacancies_id:
        recommended_vacancies = Vacancies.objects.filter(id__in=recommended_vacancies_id,
                                                         ).values('name', 'url')
    else:
        recommended_vacancies = None

    paginator = Paginator(vacanies_list, 10)
    page_number = request.GET.get('page')
    vacancies = paginator.get_page(page_number)
    # for vacancy in vacanies_list:
    #     print(vacancy['id'], user_id)
    rating_form = Rating()

    context = {
        'title': 'Your profile',
        'vacancies': vacancies,
        'rating': rating_form,
        'recommended_vacancies': recommended_vacancies,
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
