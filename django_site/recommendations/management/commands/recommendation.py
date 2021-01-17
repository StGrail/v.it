from django.core.management.base import BaseCommand
from parser_vacancies.models import Skills
from users.models import Vacancies

class Command(BaseCommand):


    def handle(self, *args, **kwargs):
        selected_vacancies = list(Vacancies.objects.filter(contains_skills=True, 
                                                           area='Москва',).values('id')) # Добавить по зарплате фильтры
        print(selected_vacancies[0], type(selected_vacancies[0]))
