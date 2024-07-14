from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, CardViewSet, CardItemViewSet


router = DefaultRouter()
router.register('boards', BoardViewSet)
router.register('cards', CardViewSet)
router.register('carditems', CardItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
