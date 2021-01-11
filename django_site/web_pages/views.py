from django.shortcuts import render


def home(request):
    context = {
        'title': 'Welcome',
        'headline': 'Home page',
    }
    return render(request, 'home.html', context)


def contacts(request):
    context = {
        'title': 'Contacts',
        'headline': 'Contacts',
    }
    return render(request, 'contacts.html', context)
