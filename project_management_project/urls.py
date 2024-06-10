from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # default
    path('admin/', admin.site.urls),

    # apps
    path('', include('core_app.urls')),
    path('', include('team_app.urls')),
    path('api/auth/', include('user.urls')),

    # api
    path('api/', include('team_app.api.urls')),
    path('api/', include('core_app.api.urls')),
]
