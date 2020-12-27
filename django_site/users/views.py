from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserCreationForm, UserChangeForm, FullReg, UpdateReg


def login(request):
    context = {
        'title': 'Login',  # title не работает
    }
    return render(request, 'login.html', context)


def join(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        full_form = FullReg(request.POST)
        if form.is_valid() and full_form.is_valid():
            form.save()
            full_form.save()
            messages.success(request, 'Вы были успешно зарегистрированы.')
            return redirect('login')
    else:
        form = UserCreationForm()
        full_form = FullReg()

    context = {
        'title': 'Join',
        'form': form,
        'full_form': full_form,
    }
    return render(request, 'join.html', context)


@login_required
def profile(request):
    context = {
        'title': 'Your profile',
    }
    return render(request, 'profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        # form = UserChangeForm(request.POST, instance=request.user)
        full_form = UpdateReg(request.POST)
        if full_form.is_valid():
            # form.save()
            full_form.save()
            messages.success(request,
                             'Ваши данные были успешно изменены.')
            return redirect('profile')
    else:
        # form = UserCreationForm(instance=request.user)
        full_form = UpdateReg()

    context = {
        'title': 'Edit',
        # 'form': form,
        'full_form': full_form,
    }
    return render(request, 'edit_profile.html', context)
