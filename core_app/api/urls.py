from django.urls import path
from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view()),
    path('projects/<pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view()),
]
