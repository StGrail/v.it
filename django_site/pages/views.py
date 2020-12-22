from django.shortcuts import render, redirect
from django.contrib import messages

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
            # try:
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # print(username)
            # print(email)
            # print(password)
            messages.success(request, 'Вы были успешно зарегистрированы.')
            return redirect('login')
    else:
        form = UserJoinForm()
    return render(request, 'join.html', {'form': form})


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
