import requests
import json

vacancies_id = []
skills_count = {}
count_processing_vacansies = 0

# Базовыый URL для запроса 
REQUEST_PER_PAGE = 1 # - Количество вакансий на одной странице
REQUEST_PAGE_COUNT = 20 # - Количество запрашиваемый страниц
request_url = f'https://api.hh.ru/vacancies?text=python+developers&experience=between1And3&per_page={REQUEST_PER_PAGE}&page='

def request_to_api(url):
    answer_hh = requests.get(url)
    return answer_hh.text


for page in range(REQUEST_PAGE_COUNT):
    short_vacansies_json = request_to_api(f'{request_url}{page}')
    short_vacansies = json.loads(short_vacansies_json)
    try:
        for vacancy in short_vacansies['items']:
            vacancy_id = vacancy['id']
            vacancies_id.append(vacancy_id)
    except:
        KeyError
        print('Глубина выборки не более 2000 вакансий')
        break

for id in vacancies_id:
    vacancy_json = request_to_api(f'https://api.hh.ru/vacancies/{id}')
    vacancy = json.loads(vacancy_json)
    for skill_dict in vacancy['key_skills']:
        try:
            count_processing_vacansies += 1
            skill = skill_dict['name'].lower()
            if skill in skills_count:
                skills_count[skill] += 1
            else:
                skills_count[skill] = 1
        except KeyError:
            continue

sorted_keys = sorted(skills_count, key=skills_count.get, reverse=True)

with open('top_50_skills_from_python_request.txt', 'w', encoding='utf-8') as res_file:
    for key in sorted_keys[:51]:
        res_file.write(f'{key} : {skills_count[key]}\n')

"""
По итогам работы программы выбираем несколько самых используемых скиллов, которые мы вытащили из ключевых навыков вакансий (key_skills)

Будем использовать
Skill : count 

1. sql
2. linux
3. git
4. postgresql
5. английский язык
6. django framework
7. flask 
8. css
9. html
10. bash
11. mysql
12. ооп
13. docker
14. mongodb
15. nginx
16. atlassian jira
17. ms excel
18. kubernetes
19. matlab
20. aws
21. scala
22. tcp/ip
23. http
24. rest
25. redis
26. unix
27. ansible
28. trello 

soft
1. работа в команде 
2. leadership skills



"""