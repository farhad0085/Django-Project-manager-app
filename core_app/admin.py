from django.contrib import admin
from .models import (
    Project,
    Card,
    CardItem,
    CardItemComment
)



def change_working_status(modeladmin, request, queryset):
    for project in queryset:
        project.working = not project.working
        project.save()
change_working_status.short_description = "Change working status"

class ProjectAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Project"""

    list_display = ['title', 'get_short_description', 'working', 'color', 'date_created']
    search_fields = ['title', 'description', 'users__username']
    actions = [change_working_status]

    def get_short_description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    get_short_description.short_description = 'Description'


class CardAdmin(admin.ModelAdmin):
    """Modify admin interface for model - Card"""

    list_display = ['title', 'get_short_description', 'project', 'created_by', 'date_created']
    search_fields = ['title', 'description', 'created_by__username', 'project__title']

    def get_short_description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    get_short_description.short_description = 'Description'

class CardItemAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItem"""

    list_display = ['title', 'get_short_description', 'card', 'created_by', 'date_created']
    search_fields = ['title', 'description', 'created_by__username', 'card__title']

    def get_short_description(self, instance):
        try:
            description = instance.description[:60]
        except:
            description = "No description available"
        return description
    get_short_description.short_description = 'Description'


class CardItemCommentAdmin(admin.ModelAdmin):
    """Modify admin interface for model - CardItemComment"""

    list_display = ['created_by', 'get_short_body', 'card_item', 'date_created']
    search_fields = ['body', 'created_by__username', 'card_item__title']

    def get_short_body(self, instance):
        return instance.body[:60]
    get_short_body.short_description = 'Comment Body'

# Register models to django admin
admin.site.register(Project, ProjectAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardItem, CardItemAdmin)
admin.site.register(CardItemComment, CardItemCommentAdmin)