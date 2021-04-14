from django.shortcuts import render


def home(request):
    user = request.user
    if user.is_anonymous is False:
        redirect = 'profile'
        button_name = 'Показать вакансии'
    else:
        redirect = 'login'
        button_name = 'Войти в it'
    context = {
        'title': 'Welcome',
        'headline': 'Home page',
        'redirect': redirect,
        'button': button_name,
    }
    return render(request, 'users/home.html', context)


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'users/contacts.html', context)
