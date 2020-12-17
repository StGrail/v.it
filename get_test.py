import requests
import json



def input_some(experience, area, skills, salary=''):
    ''' Тестируем запросы к апи'''
    if salary != '':
        salary = f'only_with_salary=true&salary={str(abs(salary))}&from'
    else:
        salary == ''
    if experience == 'no':
        experience = 'noExperience'
    if area == 'Москва':
        area = 1
    if skills is not None:
        search = f'Python+AND+{skills}'
    vacancie = requests.get(f'https://api.hh.ru/vacancies?text={search}&OR&Python&experience={experience}&area={str(area)}&{salary}').text
    vacancie_json = json.loads(vacancie)
    print(f'https://api.hh.ru/vacancies?text={search}&OR&Python&experience={experience}&area={str(area)}&{salary}')
    for item in vacancie_json['items']:
        print(item['name'])
        print(item['alternate_url'])
        print(item['salary'])
        

input_some(experience='no', area='Москва', skills='git')