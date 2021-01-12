from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    user_request = User.objects.filter(email=request.user).values('salary',
                                                                  'area',
                                                                  'experience',
                                                                  )[0]
    area = user_request['area']
    experience = user_request['experience']

    vacanies_list = Vacancies.objects.filter(area=area,
                                             experience=experience
                                             ).values('name',
                                                      'url',
                                                      ).order_by('published')

    context = {
        'title': 'Your profile',
        'vacancies_list': vacanies_list,
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
