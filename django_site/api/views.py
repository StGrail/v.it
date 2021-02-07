from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from api.serializers import UsersSerializer, VacanciesSerializer
from users.models import User
from vacancies.models import Vacancies


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class VacanciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = [
        'id_vacancy',
        'name',
        'area',
        'experience',
        'salary_from',
        'salary_to',
        'url',
        'published',
    ]
    ordering_fields = ['published']
