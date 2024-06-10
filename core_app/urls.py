from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, CardViewSet, CardItemViewSet, ProjectCardListAPIView


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('cards', CardViewSet)
router.register('carditems', CardItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('projects/<project_id>/cards/', ProjectCardListAPIView.as_view())
]
