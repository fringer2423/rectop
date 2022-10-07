from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls.user_urls', namespace='api')),
    path('api/', include('apps.api.urls.swagger_urls', namespace='api_swagger')),
]
