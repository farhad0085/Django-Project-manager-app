from django.contrib import admin
from .models import (
    Board,
    Card,
    CardItem,
    CardItemComment
)


class BoardAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Project"""

    list_display = ['title', '_description', 'working', 'color', 'created_at']
    search_fields = ['title', 'description', 'users__username']
    
    def _description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    _description.short_description = 'Description'


class CardAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Card"""

    list_display = ['title', '_description', 'board', 'created_by', 'created_at']
    search_fields = ['title', 'description', 'created_by__username', 'board__title']

    def _description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    _description.short_description = 'Description'

class CardItemAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItem"""

    list_display = ['title', '_description', 'card', 'created_by', 'created_at']
    search_fields = ['title', 'description', 'created_by__username', 'card__title']

    def _description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    _description.short_description = 'Description'


class CardItemCommentAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItemComment"""

    list_display = ['created_by', 'get_short_body', 'card_item', 'created_at']
    search_fields = ['body', 'created_by__username', 'card_item__title']

    def get_short_body(self, instance):
        return instance.body[:60]
    get_short_body.short_description = 'Comment Body'

# Register models to django admin
admin.site.register(Board, BoardAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardItem, CardItemAdmin)
admin.site.register(CardItemComment, CardItemCommentAdmin)