from django.shortcuts import render


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


# def join(request):
#     context = {
#         'title': 'Join',
#         'headline': 'Join page',
#     }
#     return render(request, 'join.html', context)


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
