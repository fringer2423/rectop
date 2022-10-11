from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.api.urls.user_urls', namespace='user_endpoints')),
    path('api/', include('apps.api.urls.swagger_urls', namespace='api_swagger')),
    path('api/company/', include('apps.api.urls.company_urls', namespace='company_endpoints')),
    path('api/branch/', include('apps.api.urls.branch_urls', namespace='branch_endpoints')),
]
