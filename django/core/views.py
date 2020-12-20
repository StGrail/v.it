from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


def join(request):
    return render(request, 'join.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})
