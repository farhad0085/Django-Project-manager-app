from django.urls import path, re_path
from .views import (
    home,
    pages,
    list_projects,
    create_project,
    detail_project,
    create_card,
    delete_card,
    create_card_item,
    delete_card_item
)

urlpatterns = [
    path('', home, name="home"),
    re_path(r'^.*\.html', pages, name='pages'),

    # project
    path('projects/', list_projects, name='list_projects'),
    path('projects/new/', create_project, name='create_project'),
    path('projects/<id>/', detail_project, name='detail_project'),

    # card
    path('cards/new/project/<project_id>/', create_card, name='create_card'),
    path('cards/delete/project/<project_id>/card/<card_id>/', delete_card, name='delete_card'),

    # card item
    path('card-item/new/project/<project_id>/card/<card_id>/', create_card_item, name='create_card_item'),
    path('card-item/delete/project/<project_id>/card-item/<card_item_id>/', delete_card_item, name='delete_card_item'),
]
