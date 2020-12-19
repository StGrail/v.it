import requests
import json
import urllib


params = {
    'User-Agent': 'api-test-agent',
    'currency': 'RUR',
    # 'from': 'cluster_compensation',
    # 'showClusters': 'true',
}

def input_some(skill='Python', area='Москва', experience='no', salary_from=''):
    ''' Тестируем запросы к апи'''
    if skill != 'Python':
        params['text'] = f'Python {skill}'  
    else:
        params['text'] = skill
    if area == 'Москва':
        params['area'] = 1
    if experience == 'no':
        params['experience'] = 'noExperience'
    if salary_from != '':
        params['only_with_salary'] = 'true'
        params['salary'] = f'{abs(salary_from)}'
        params['from'] = f'{abs(salary_from)}'
    else:
        salary_from = salary_from

    url = 'https://api.hh.ru/vacancies'
    vacancy = requests.get(url, params=urllib.parse.urlencode(params))
    vacancy_text = vacancy.text 
    vacancy_json = json.loads(vacancy_text)
    for item in vacancy_json['items']:
        print(item['name']) 
        print(item['alternate_url'])
        print(item['salary'])
        print(item['type'])
        

input_some(skill='git', salary_from=180000)
