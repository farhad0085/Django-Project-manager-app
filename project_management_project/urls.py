from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # default
    path('admin/', admin.site.urls),

    # api
    path('api/auth/', include('user.urls')),
    path('api/', include('board.urls')),
]
