from datetime import date

from vacancies.models import Vacancies
from parser_vacancies.models import VacanciesCount
from parser_vacancies.management.commands import config_parser


def check_vacancies_table():
    vacancies_count = Vacancies.objects.filter().count()
    if vacancies_count:
        url_to_parser = config_parser.REQUEST_URL_PERIOD
        return url_to_parser, vacancies_count
    print('Database is empty')
    url_to_parser = config_parser.REQUEST_URL
    return url_to_parser, vacancies_count


def save_vacancies_count_to_db(added_today, total_vacancies_count):
    row_vacancies_count = VacanciesCount(
        date=date.today(),
        added_today=added_today,
        total_vacancies_count=total_vacancies_count
    )
    row_vacancies_count.save()
