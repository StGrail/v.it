from django.test import TestCase

from api.serializers import VacanciesSerializer
from vacancies.models import Vacancies


class VacanciesSerializerTestCase(TestCase):
    def test_vacancies(self):
        """ Тестируем  """

        vacancy_1 = Vacancies.objects.create(
            id_vacancy=1, name='PythonDev1', area='Москва', experience='от 1 года до 3 лет',
            salary_from='0', salary_to='100000', url='PythonDev1.com', published='2021-02-25T17:26:17+03:00',
            contains_skills=False
        )
        vacancy_2 = Vacancies.objects.create(
            id_vacancy=2, name='PythonDev2', area='Москва', experience='от 1 года до 3 лет',
            salary_from='0', salary_to='100000', url='PythonDev2.com', published='2021-02-25T17:26:17+03:00',
            contains_skills=False
        )
        data = VacanciesSerializer([vacancy_1, vacancy_2], many=True).data
        expected_data = [
            {
                "id_vacancy": vacancy_1.id,
                "name": 'PythonDev1',
                "area": 'Москва',
                "experience": "от 1 года до 3 лет",
                "salary_from": "0",
                "salary_to": "100000",
                "url": 'PythonDev1.com',
                "published": "2021-02-25T17:26:17+03:00",
                "contains_skills": False
            },
            {
                "id_vacancy": vacancy_2.id,
                "name": 'PythonDev2',
                "area": 'Москва',
                "experience": "от 1 года до 3 лет",
                "salary_from": "0",
                "salary_to": "100000",
                "url": 'PythonDev2.com',
                "published": "2021-02-25T17:26:17+03:00",
                "contains_skills": False
            },

        ]
        self.assertEqual(expected_data, data)
