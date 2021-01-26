from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from recommendation.recommendation_services import recommendations
from users.forms import UserCreationForm, UserChangeForm, Rating
from .models import User, Vacancies
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
    vacanies_list, recommended_vacancies = profile_view(user_request)
    paginator = Paginator(vacanies_list, 10)
    page_number = request.GET.get('page')
    vacancies = paginator.get_page(page_number)
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

#Зачаток фукнции для обработки запроса с кнопочек-звездочек
# def processing_rating(request):
#     if request.method == 'GET':
#         rating = request.GET['rating']
        