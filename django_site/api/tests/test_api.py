import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import VacanciesSerializer
from users.models import User
from vacancies.models import Vacancies


class VacanciesApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user')
        self.vacancy_1 = Vacancies.objects.create(
            id_vacancy='1', name='python developer1',
            area='Москва', experience='no_experience',
            salary_from='50000', salary_to='100000',
            published='2021-01-01T00:00:00+03:00', contains_skills=False
        )
        self.vacancy_2 = Vacancies.objects.create(
            id_vacancy='2', name='python developer2',
            area='Москва', experience='no_experience',
            salary_from='50000', salary_to='100000',
            published='2021-01-01T00:10:00+03:00', contains_skills=False
        )
        self.vacancy_3 = Vacancies.objects.create(
            id_vacancy='3', name='python developer3',
            area='Москва', experience='no_experience',
            salary_from='50000', salary_to='100000',
            published='2021-01-01T00:12:00+03:00', contains_skills=False
        )

    def test_get_vacancies(self):
        url = reverse('vacancies-list')
        response = self.client.get(url, data={'area': 'Москва'})
        serializer_data = VacanciesSerializer([self.vacancy_1,
                                               self.vacancy_2,
                                               self.vacancy_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('vacancies-list')
        response = self.client.get(url, data={'ordering': '-published'})
        serializer_data = VacanciesSerializer([self.vacancy_1,
                                               self.vacancy_2,
                                               self.vacancy_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertNotEqual(serializer_data, response.data)
