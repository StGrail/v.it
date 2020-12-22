from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm


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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} зарегистрирован!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'join.html', {'form': form})


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
