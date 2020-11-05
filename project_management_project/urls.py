from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('core_app.urls')),
    path('api/', include('core_app.api.urls')),
]
