from django.contrib import admin
from .models import (
    Project,
    Card,
    CardItem,
    CardItemComment
)


class ProjectAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Project"""

    list_display = ['id', 'title', 'get_short_description', 'date_created']
    search_fields = ['title', 'description', 'users__username']

    def get_short_description(self, instance):
        return instance.description[:60]


class CardAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Card"""

    list_display = ['id', 'title', 'get_short_description', 'project', 'created_by', 'date_created']
    search_fields = ['title', 'description', 'created_by__username', 'project__title']

    def get_short_description(self, instance):
        return instance.description[:60]


class CardItemAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItem"""

    list_display = ['id', 'title', 'get_short_description', 'card', 'created_by', 'date_created']
    search_fields = ['title', 'description', 'created_by__username', 'card__title']

    def get_short_description(self, instance):
        return instance.description[:60]


class CardItemCommentAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItemComment"""

    list_display = ['id', 'created_by', 'get_short_body', 'card_item', 'date_created']
    search_fields = ['body', 'created_by__username', 'card_item__title']

    def get_short_body(self, instance):
        return instance.body[:60]


# Register models to django admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardItem, CardItemAdmin)
admin.site.register(CardItemComment, CardItemCommentAdmin)