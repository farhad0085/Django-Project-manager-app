from django.urls import path, re_path
from .views import home, pages, list_projects, create_project, detail_project

urlpatterns = [
    path('', home, name="home"),
    re_path(r'^.*\.html', pages, name='pages'),

    # project
    path('projects/', list_projects, name='list_projects'),
    path('projects/new/', create_project, name='create_project'),
    path('projects/<id>/', detail_project, name='detail_project'),
]
