from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, CardViewSet, CardItemViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('cards', CardViewSet)
router.register('carditems', CardItemViewSet)

urlpatterns = [
    path('core/', include(router.urls)),
]
