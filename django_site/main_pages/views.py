from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserJoinForm, UserFullRegistationForm


def home(request):
    context = {
        'title': 'Welcome',
        'headline': 'Home page',
    }
    return render(request, 'home.html', context)


def login(request):
    context = {
        'title': 'Login',
        'headline': 'login page',
    }
    return render(request, 'login.html', context)


def join(request):  # Проверку на полную регистрацию, если нет, то редирект.
    if request.method == 'POST':
        form = UserJoinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы были успешно зарегистрированы.')
            return redirect('login')
    else:
        form = UserJoinForm()
    return render(request, 'join.html', {'form': form})


@login_required
def profile(request):  # Нужно заменить "профиль" на окончание регистрации.
    if request.method == 'POST':
        full_form = UserFullRegistationForm(request.POST,
                                            instance=request.user.profile)
        if full_form.is_valid():
            full_form.save()
            messages.success(request,
                             'Вы были успешно закончили зарегистрацию.')
            return redirect('home')  # Заменить на редирект в профиль.
    else:
        full_form = UserFullRegistationForm(instance=request.user.profile)

    context = {
        'full_form': full_form,
    }
    return render(request, 'profile.html', context)


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
