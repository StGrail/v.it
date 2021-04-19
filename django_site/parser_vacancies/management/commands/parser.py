import json
import re

from django.core.management.base import BaseCommand
from django.db import DatabaseError
from django.db.utils import IntegrityError
from vacancies.models import Vacancies
from parser_vacancies.management.commands import checking_vacancies_count as cvc
from parser_vacancies.management.commands import checking_vacancy_for_skills as cv
from parser_vacancies.management.commands import config_parser
from parser_vacancies.models import Skills

import requests


class Command(BaseCommand):

    def get_request_data(self, url: str) -> dict:
        try:
            answer_hh = requests.get(url)
            answer_hh.raise_for_status()
        except(requests.RequestException):
            print('Network error')
        return json.loads(answer_hh.text)

    def check_vacancies_table(self):
        vacancies_count = Vacancies.objects.filter().count()
        if vacancies_count:
            print('Vacancies count in database: ', vacancies_count)
            url_to_parser = config_parser.REQUEST_URL_PERIOD
            return url_to_parser
        print('Database is empty')
        url_to_parser = config_parser.REQUEST_URL
        return url_to_parser

    def get_vacancy_data(self, id_vacancy: int, vacancy: dict, contains_skills: bool) -> dict:
        """
        Принимает на вход id вакансии, полное представление вакансии ввиде словаря, индикатор наличия скиллов.
        Возвращает словарь полей вакансии, которые будут записаны в таблицу vacancies БД.
        """
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

    def save_vacancy_data_in_db(self, vacancy_data: dict, skills_dict: dict):
        """
        Принимает на вход поля вакансии, подлежащие сохранению в БД в виде словаря
        Выполняет сохранение вакансии в БД
        """
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

    def check_vacancy_name(self, vacancy_name: str) -> bool:
        """
        Фукнция, которая проверяет название вакансии на предмет
        наличия слов, которые показывают, что вакансия не имеет отношения
        к python
        """
        vacancy_name = vacancy_name.lower()
        vacancy_name = re.split(r'[\.\s\(\):,-/]+', vacancy_name)
        if 'python' in vacancy_name:
            return True
        for word in vacancy_name:
            if word in config_parser.NOT_PYTHON:
                return False
        return True

    def processing_vacancies_in_page(self, short_vacancies: dict):
        """
       Функция, которая принимает на вход словарь, содержащий
       вакансии в коротком представлении со страницы page, обрабатывает их
       с помощью дополнительных функций и сохраняет в БД
        """
        for short_vacancy in short_vacancies['items']:
            contains_skills = False
            if short_vacancy['archived']:
                continue
            try:
                vacancy_id = short_vacancy['id']
                vacancy_name = short_vacancy['name']
            except KeyError:
                print('Глубина выборки не более 2000 вакансий')
                break
            is_python_vacancy = self.check_vacancy_name(vacancy_name)
            if not is_python_vacancy:
                continue
            vacancy = self.get_request_data(f'https://api.hh.ru/vacancies/{vacancy_id}')
            skills_dict, contains_skills = cv.is_skill_in_list(vacancy)
            vacancy_data = self.get_vacancy_data(vacancy_id, vacancy, contains_skills)
            self.save_vacancy_data_in_db(vacancy_data, skills_dict)

    def handle(self, *args, **kwargs):
        """Функция, запускающая парсер"""
        print('Start vacancies parser')
        url_to_parser, vacancies_count_before_adding = cvc.check_vacancies_table()
        for page in range(config_parser.REQUEST_PAGE_COUNT):
            print(f'Used query: {url_to_parser}{page}')
            short_vacancies = self.get_request_data(f'{url_to_parser}{page}')
            if not short_vacancies['items']:
                break
            self.processing_vacancies_in_page(short_vacancies)
        vacancies_count_after_adding = cvc.check_vacancies_table()[1]
        vacancies_added_today_count = vacancies_count_after_adding - vacancies_count_before_adding
        cvc.save_vacancies_count_to_db(vacancies_added_today_count, vacancies_count_after_adding)
        print(f'Today added {vacancies_added_today_count} vacancies. Total {vacancies_count_after_adding} vacancies')
        print('Vacancies parser completed')
