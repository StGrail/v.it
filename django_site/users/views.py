from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse

from recommendation.recommendation_services import recommendations
from users.forms import UserCreationForm, UserChangeForm
from .models import User, Vacancies, Rating
from .services import profile_view


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
    vacancies_list, recommended_vacancies = profile_view(user_request)
    paginator = Paginator(vacancies_list, 10)
    page_number = request.GET.get('page')
    vacancies = paginator.get_page(page_number)
    rating = Rating.objects.filter(id=request.user.id).values('rating')[0]['rating']
    context = {
        'title': 'Your profile',
        'vacancies': vacancies,
        'rating': rating,
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

# Зачаток фукнции для обработки запроса с кнопочек-звездочек
