from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomeView(View):
    template_name = 'users/home.html'

    def get(self, request):
        user = request.user
        if user.is_anonymous is False:
            redirect = 'profile'
            button_name = 'Показать вакансии'
        else:
            redirect = 'login'
            button_name = 'Войти в it'
        context = {
            'title': 'Welcome',
            'redirect': redirect,
            'button': button_name,
        }

        return render(request, self.template_name, context=context)


class ContactsView(TemplateView):
    template_name = 'users/contacts.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': 'Contacts',
        }
        return context
