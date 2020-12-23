from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserJoinForm


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


def join(request):
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
def profile(request):
    return render(request, 'profile.html')


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
