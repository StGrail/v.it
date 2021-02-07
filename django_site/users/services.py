from users.models import User
from vacancies.models import Vacancies
from recommendation.recommendation_services import recommendations


def remove_user_from_vacancy_relation(user: 'class users.models.User'):
    """
    Функция, которая удаляет связь пользователя с просмотренными им вакансиями в том случае,
    если пользователь изменил параметры поиска вакансий.
    """
    vacancies = Vacancies.objects.filter(shown_to_users=user)
    for vacancy in vacancies:
        vacancy.shown_to_users.remove(user)


def update_shown_vacancy_to_user(user_id: int, vacancies_list: 'Queryset'):
    """
    Функция, которая сохраняет в БД данные о вакансиях, показанных конкретному
    пользователю
    """
    user = User.objects.get(id=user_id)
    for vacancy in vacancies_list:
        vacancy = Vacancies.objects.get(id=vacancy['id'])
        vacancy.shown_to_users.add(user)


def profile_view(user_request: 'Queryset') -> 'Queryset':
    """
    Функция, которая производит обработку данных пользователя и выборку из БД
    вакансий для конкретного пользователя
    """
    user_id = user_request[0]['id']
    area = user_request[0]['area']
    experience = user_request[0]['experience']
    salary = user_request[0]['salary']
    without_salary = user_request[0]['without_salary']

    if without_salary is False:
        vacancies_list = Vacancies.objects.filter(area=area,
                                                  experience=experience,
                                                  salary_from__lte=salary,
                                                  salary_to__gte=salary,
                                                  ).exclude(banned_by_users=user_id,
                                                            ).values('name',
                                                                     'url',
                                                                     'id',
                                                                     ).order_by('-published')
    else:
        vacancies_list = Vacancies.objects.filter(area=area,
                                                  experience=experience,
                                                  ).exclude(banned_by_users=user_id,
                                                            ).values('name',
                                                                     'url',
                                                                     'id',
                                                                     ).order_by('-published')
    update_shown_vacancy_to_user(user_id, vacancies_list)
    recommended_vacancies_id = recommendations(user_request)
    if recommended_vacancies_id:
        recommended_vacancies = Vacancies.objects.filter(id__in=recommended_vacancies_id,
                                                         ).values('name', 'url')
    else:
        recommended_vacancies = None
    return vacancies_list, recommended_vacancies

