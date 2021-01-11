import requests
import json
from django.db import IntegrityError

from users.models import Vacancies


def input_request(experience='noExperience',
                  skill='Python',
                  area='Москва',
                  salary_from=''):
    """ Выполняем запрос на хх.апи с данными пользователя и получаем список
        id вакансий, который подходят под этот запрос."""
    params = {
        'User-Agent': 'api-test-agent',
    }
    if skill != 'Python':
        params['text'] = f'Python+AND+{skill}'
    else:
        params['text'] = skill
    if area == 'Москва':
        params['area'] = 1
    if salary_from != '':
        params['only_with_salary'] = 'true'
        params['salary'] = f'{salary_from}&from'
    else:
        salary_from = salary_from

    vacancy_request = requests.get('https://api.hh.ru/vacancies',
                                   params=params)
    vacancy_url = requests.utils.unquote(vacancy_request.url)
    vacancy_text = requests.get(vacancy_url).text
    vacancy_json = json.loads(vacancy_text)

    vacancy_id_list = [vacancy_list['id'] for vacancy_list in vacancy_json['items']]

    return vacancy_id_list


def search_and_save(request, vacancy_id_list):  # Сдлеать проверку на вхождение id в бд.
    # vacancy_id_in_db = Vacancies.objects.filter(user=request.user).values('vacancy_id')
    for elmnt in vacancy_id_list:
        try:
            header = {'User-Agent': 'api-test-agent'}
            link = f'https://api.hh.ru/vacancies/{elmnt}'
            full_vacancy = json.loads(requests.get(f'{link}', header).text)
            row = Vacancies(vacancy_id=full_vacancy['id'],
                            name=full_vacancy['name'],
                            area=full_vacancy['area']['name'],
                            url=full_vacancy['alternate_url'],
                            user=request.user
                            )
            row.save()
        except IntegrityError:
            pass
