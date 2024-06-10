from rest_framework.permissions import BasePermission


class IsOwnProject(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user in obj.users.all():
            return True
        return False
    