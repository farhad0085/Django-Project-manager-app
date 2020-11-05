from django.urls import path
from django.urls.conf import include
from .views import TeamViewSet
from core_app.api.urls import router
router.register('teams', TeamViewSet)

urlpatterns = [
    path('', include(router.urls))
]
