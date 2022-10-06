from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('api/', include('apps.api.urls.user_urls')),
    path('api/', include('apps.api.urls.swagger_urls')),
]
