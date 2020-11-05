from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    """Modify default model admin for team model"""

    list_display = ['name', 'get_total_member', 'date_created']
    search_fields = ['name', 'member__username']

    def get_total_member(self, instance):
        return instance.member.all().count()
    get_total_member.short_description = "Total member"

admin.site.register(Team, TeamAdmin)
