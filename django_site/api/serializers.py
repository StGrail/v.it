from rest_framework.serializers import ModelSerializer

from users.models import User
from vacancies.models import Vacancies


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'area',
            'salary',
            'without_salary',
            'experience',
            'skills'
        ]


class VacanciesSerializer(ModelSerializer):
    class Meta:
        model = Vacancies
        fields = [
            'id_vacancy',
            'name',
            'area',
            'experience',
            'salary_from',
            'salary_to',
            'url',
            'published',
            'contains_skills'
        ]
