from rest_framework.routers import SimpleRouter
from . import views as api_views

router = SimpleRouter()
router.register(r'api/user', api_views.UserViewSet)
router.register(r'api/vacancy', api_views.VacanciesViewSet)
