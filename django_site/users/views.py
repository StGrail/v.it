from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, UserChangeForm


def login(request):
    context = {
        'title': 'Login',  # title не работает
    }
    return render(request, 'login.html', context)


def join(request):
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
    context = {
        'title': 'Your profile',
    }
    return render(request, 'profile.html', context)


@login_required  # Применяется не та форма.
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Ваши данные были успешно изменены.')
            return redirect('profile')
    else:
        form = UserCreationForm(instance=request.user)

    context = {
        'title': 'Edit',
        'form': form,
    }
    return render(request, 'edit_profile.html', context)
