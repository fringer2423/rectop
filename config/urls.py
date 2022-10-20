from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import apps.core.views

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.api.urls.user_urls', namespace='user_endpoints')),
    path('api/', include('apps.api.urls.swagger_urls', namespace='api_swagger')),
    path('api/company/', include('apps.api.urls.company_urls', namespace='company_endpoints')),
    path('api/branch/', include('apps.api.urls.branch_urls', namespace='branch_endpoints')),
    path('api/telebot/', include('apps.api.urls.telebot_urls', namespace='telebot_endpoints')),
    path('api/connect/', include('apps.api.urls.connect_urls', namespace='connect_endpoints')),
    path('api/review/', include('apps.api.urls.review_urls', namespace='review_endpoints')),
    path('api/review_settings/', include('apps.api.urls.review_settings_urls', namespace='review_settings_endpoints')),
    path('api/answer/', include('apps.api.urls.answer_urls', namespace='answer_endpoints')),
    path('api/qrcode/', include('apps.api.urls.qrcode_urls', namespace='qrcode_endpoints')),
    path('api/rate_info/', include('apps.api.urls.rate_info_urls', namespace='rate_info_endpoints')),
    path('api/rate/', include('apps.api.urls.rate_urls', namespace='rate_endpoints')),

    path('test/ping/', apps.core.views.ping, name='ping'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
