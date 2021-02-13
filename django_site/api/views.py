from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from vacancies.models import Vacancies


from users.models import User
from .serializers import UsersSerializer, VacanciesSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VacanciesViewSet(ModelViewSet):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_fields = [
        'name',
        'area',
        'experience',
        'salary_from',
        'salary_to',
        'published',
    ]
    ordering_fields = ['published']
