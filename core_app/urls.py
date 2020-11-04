from django.urls import path, re_path
from .views import home, pages

urlpatterns = [
    path('', home, name="home"),
    re_path(r'^.*\.html', pages, name='pages'),
]
