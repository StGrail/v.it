from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from vacancies.models import Vacancies


from users.models import User
from .serializers import UsersSerializer, VacanciesSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class VacanciesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = [
        'name',
        'area',
        'experience',
        'salary_from',
        'salary_to',
        'published',
    ]
    ordering_fields = ['published']
