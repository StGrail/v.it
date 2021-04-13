from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from vacancies.models import Vacancies, Rating
from .forms import UserCreationForm, UserChangeForm
from .models import User
from .services import profile_view, remove_user_from_vacancy_relation, pagination, stars_rating


class JoinForm(View):
    """ Регистрации юзера с последующим редиректом на страницу логина. """

    form_class = UserCreationForm
    template_name = 'join.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'title': 'Join', 'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы были успешно зарегистрированы.')
            return redirect('login')
        else:
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class EditProfile(View):
    """ Изменение данных профиля в лк. """

    form_class = UserChangeForm
    template_name = 'edit_profile.html'

    def get(self, request):
        form = self.form_class(instance=request.user)
        return render(request, self.template_name, {'title': 'Edit', 'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Ваши данные были успешно изменены.')
            user_request = User.objects.get(email=request.user)
            remove_user_from_vacancy_relation(user_request)
            return redirect('profile')
        else:
            form = self.form_class(instance=request.user)

        return render(request, self.template_name, {'form': form})


@login_required
def profile(request):
    """ Профиль юзера с выводом вакансий для него. """

    user_request = User.objects.filter(email=request.user).values('id',
                                                                  'area',
                                                                  'salary',
                                                                  'experience',
                                                                  'skills',
                                                                  'without_salary',
                                                                  )
    vacancies_list, recommended_vacancies = profile_view(user_request)
    page_number = request.GET.get('page')
    vacancies = pagination(vacancies_list, page_number)

    for item in vacancies_list:
        rating_qs = Rating.objects.filter(user=request.user.id, vacancy=item['id']).values('rating')
        item["rating"] = rating_qs[0]['rating'] if rating_qs else 0

    context = {
        'title': 'Your profile',
        'vacancies': vacancies,
        'recommended_vacancies': recommended_vacancies,
    }
    return render(request, 'profile.html', context)


@login_required
@require_http_methods(["POST"])
@csrf_exempt
def rate_vacancy(request):
    """ Оценка вакансии пользователем. """

    rating = request.POST.get('rate')
    vacancy = Vacancies.objects.get(pk=request.POST.get('vacancy'))
    user = User.objects.get(pk=request.user.id)
    stars_rating(rating, vacancy, user)
    return HttpResponse()
