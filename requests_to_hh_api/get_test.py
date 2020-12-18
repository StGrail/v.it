import requests
import json


params = {
    'User-Agent': 'api-test-agent',
    }

def input_some(skill='Python', area='Москва', experience='no', salary_from=''):
    ''' Тестируем запросы к апи'''
    if skill != 'Python':
        params['text'] = f'Python+AND+{skill}'  
    else:
        params['text'] = skill
    if area == 'Москва':
        params['area'] = 1
    if experience == 'no':
        params['experience'] = 'noExperience'
    if salary_from != '':
        params['only_with_salary'] = 'true'
        params['salary'] = f'{str(abs(salary_from))}&from'
    else:
        salary_from = salary_from

    vacancy = requests.get(f'https://api.hh.ru/vacancies', params=params)
    vacancy_url = requests.utils.unquote(vacancy.url)
    vacancy_text = requests.get(vacancy_url).text
    vacancy_json = json.loads(vacancy_text)
    for item in vacancy_json['items']:
        print(item['name'])
        print(item['alternate_url'])
        print(item['salary'])
        print(item['type'])
        

input_some(skill='git', salary_from=20000)
