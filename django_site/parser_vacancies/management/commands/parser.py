from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from users.models import Vacancies
from parser_vacancies.management.commands import checking_vacancy_for_skills as cv
from parser_vacancies.management.commands import config_parser
from parser_vacancies.models import Skills

import json
import requests


class Command(BaseCommand):

    def get_request_data(self, url):
        answer_hh = requests.get(url).text
        return json.loads(answer_hh)


    def get_vacancy_data(self, id_vacancy, vacancy, contains_skills):
        '''
        Принмает на вход id вакансии, полное представление вакансии ввиде словаря, индикатор наличия скиллов.
        Возвращает словарь полей вакансии, которые будут записаны в таблицу vacancies БД.
        '''
        vacancy_data = {'id_vacancy': id_vacancy}
        if contains_skills:
            vacancy_data['contains_skills'] = True
        else:
            vacancy_data['contains_skills'] = False
        vacancy_data['experience'] = vacancy['experience']['name'].lower()
        if vacancy['salary'] and vacancy['salary']['from']:
            vacancy_data['salary_from'] = vacancy['salary']['from']
        else:
            vacancy_data['salary_from'] = ''
        if vacancy['salary'] and vacancy['salary']['to']:
            vacancy_data['salary_to'] = vacancy['salary']['to']
        else:
            vacancy_data['salary_to'] = ''
        vacancy_data['name'] = vacancy['name']
        vacancy_data['area'] = vacancy['area']['name']
        vacancy_data['published'] = vacancy['published_at']
        vacancy_data['alternate_url'] = vacancy['alternate_url']
        return vacancy_data


    def save_vacancy_data_in_db(self, vacancy_data, skills_dict):
        '''
        Принимает на вход поля вакансии, подлежащие сохранению в БД в виде словаря
        Выполняет сохранение вакансии в БД
        '''
        row_vacancy = Vacancies(
                        id_vacancy=vacancy_data['id_vacancy'],
                        name=vacancy_data['name'],
                        area=vacancy_data['area'],
                        experience=vacancy_data['experience'],
                        salary_from=vacancy_data['salary_from'],
                        salary_to=vacancy_data['salary_to'],
                        url=vacancy_data['alternate_url'],
                        published=vacancy_data['published'],
                        contains_skills=vacancy_data['contains_skills'],
                        )
        try:
           row_vacancy.save()
        except IntegrityError:
           print(f"Vacancy with id {vacancy_data['id_vacancy']} is contained in the database")
           return
        if vacancy_data['contains_skills']:
            row_vacancy_skills = Skills(
                        id_vacancy=row_vacancy,
                        sql=skills_dict['sql'],
                        linux=skills_dict['linux'],
                        git=skills_dict['git'],
                        postgresql=skills_dict['postgresql'],
                        django=skills_dict['django'],
                        flask=skills_dict['flask'],
                        css=skills_dict['css'],
                        html=skills_dict['html'],
                        bash=skills_dict['bash'],
                        mysql=skills_dict['mysql'],
                        oop=skills_dict['oop'],
                        docker=skills_dict['docker'],
                        mongodb=skills_dict['mongodb'],
                        pandas=skills_dict['pandas'],
                        numpy=skills_dict['numpy'],
                        jira=skills_dict['jira'],
                        kubernetes=skills_dict['kubernetes'],
                        http=skills_dict['http'],
                        tcp_ip=skills_dict['tcp_ip'],
                        trello=skills_dict['trello'],
                        unix=skills_dict['unix'],
                        redis=skills_dict['redis'],
                        )
            row_vacancy_skills.save()
            


    def processing_vacancies_in_page(self, short_vacancies):
        '''
        Принимает на вход счетчик вакансий и словарь вакансий с страницы page.
        Возвращает значения счетчика вакансий и список, содержащий строки столбцов и значений
        SQL команды для записи в таблицу vacancies БД
        '''
        for short_vacancy in short_vacancies['items']:
            contains_skills = False
            if short_vacancy['archived']:
                continue
            try:
                vacancy_id = short_vacancy['id']
            except KeyError:
                print('Глубина выборки не более 2000 вакансий')
                break
            vacancy = self.get_request_data(f'https://api.hh.ru/vacancies/{vacancy_id}')
            skills_dict, contains_skills = cv.is_skill_in_list(vacancy)
            #if skills_dict:
            #    contains_skills = True
            vacancy_data = self.get_vacancy_data(vacancy_id, vacancy, contains_skills)
            self.save_vacancy_data_in_db(vacancy_data, skills_dict)


    def handle(self, *args, **kwargs):
        count_vacancies = 0
        print('Start vacancies parser')
        for page in range(config_parser.REQUEST_PAGE_COUNT):
            short_vacancies = self.get_request_data(f'{config_parser.REQUEST_URL}{page}')
            count = self.processing_vacancies_in_page(short_vacancies)
            count_vacancies += len(short_vacancies['items'])
        print('Vacancies parser complited')
