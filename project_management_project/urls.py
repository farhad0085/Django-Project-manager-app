from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # default
    path('admin/', admin.site.urls),

    # apps
    path('', include('authentication.urls')),
    path('', include('core_app.urls')),
    path('', include('team_app.urls')),

    # api
    path('api/', include('team_app.api.urls')),
    path('api/', include('core_app.api.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration', include('rest_auth.registration.urls')),
]
