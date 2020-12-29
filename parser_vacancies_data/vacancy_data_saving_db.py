import config
import checking_vacancy_for_skills as cv
import json
import psycopg2
from psycopg2.errors import UniqueViolation, InFailedSqlTransaction
import requests
import sql_query_for_save_data as sql_save


def get_request_data(url):
    answer_hh = requests.get(url).text
    return json.loads(answer_hh)


def processing_vacancies_list(count, short_vacancies):
    '''
    Принимает на вход счетчик вакансий и словарь вакансий с страницы page.
    Возвращает значения счетчика вакансий и список, содержащий строки столбцов и значений
    SQL команды для записи в таблицу vacancies БД
    '''
    string_for_SQL_list = []
    for short_vacancy in short_vacancies['items']:
        count += 1
        print(count)
        if short_vacancy['archived']:
            continue
        try:
            vacancy_id = short_vacancy['id']
        except KeyError:
            print('Глубина выборки не более 2000 вакансий')
            break
        vacancy = get_request_data(f'https://api.hh.ru/vacancies/{vacancy_id}')
        skill_dict = cv.is_skill_in_list(vacancy)
        if not skill_dict:
            continue
        vacancy_data = sql_save.get_vacancy_data(vacancy_id, skill_dict, vacancy)
        string_for_SQL = sql_save.create_SQL_query(count, vacancy_data)
        string_for_SQL_list.append(string_for_SQL)
    return count, string_for_SQL_list


count = 0
con = psycopg2.connect(**config.DATABASE)
cur = con.cursor()
for page in range(config.REQUEST_PAGE_COUNT):
    short_vacancies = get_request_data(f'{config.REQUEST_URL}{page}')
    count, string_for_SQL_list = processing_vacancies_list(count, short_vacancies)
    if not string_for_SQL_list:
        continue
    for string_for_SQL in string_for_SQL_list:
        try:
            cur.execute(f'INSERT INTO vacancies ({string_for_SQL[0]}) VALUES ({string_for_SQL[1]})')
        except (UniqueViolation, InFailedSqlTransaction):
            print('Значения в столбцах id и id_vacancy должны быть уникальными')
            continue
con.commit()
con.close()
        
        



