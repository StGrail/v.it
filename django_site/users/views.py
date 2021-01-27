from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse

from users.forms import UserCreationForm, UserChangeForm
from .models import User, Rating, Vacancies
from .services import profile_view, remove_user_from_vacancy_relation


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
    for item in vacancies_list:
        rating_qs = Rating.objects.filter(user=request.user.id, vacancy=item['id']).values('rating')
        item["rating"] = rating_qs[0]['rating'] if rating_qs else 0
    paginator = Paginator(vacancies_list, 10)
    page_number = request.GET.get('page')
    vacancies = paginator.get_page(page_number)
    context = {
        'title': 'Your profile',
        'vacancies': vacancies,
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
            user_request = User.objects.get(email=request.user)
            remove_user_from_vacancy_relation(user_request)
            return redirect('profile')
    else:
        edit_form = UserChangeForm(instance=request.user)

    context = {
        'title': 'Edit',
        'edit_form': edit_form,
    }
    return render(request, 'edit_profile.html', context)

@login_required
@require_http_methods(["POST"])
@csrf_exempt
def rate_vacancy(request):
    rating = request.POST.get('rating')
    vacancy = Vacancies.objects.get(pk=request.POST.get('vacancy'))
    user = User.objects.get(pk=request.user.id)
    rating_qs = Rating.objects.filter(user=user, vacancy=vacancy)
    if not rating_qs:
        rating = Rating(user=user, vacancy=vacancy, rating=rating)
        rating.save()
    else:
        rating_qs.update(rating=rating)
    return HttpResponse()



