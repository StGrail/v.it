from rest_framework.routers import SimpleRouter
from . import views as api_views

router = SimpleRouter()
router.register(r'user', api_views.UserViewSet)
router.register(r'vacancy', api_views.VacanciesViewSet)
