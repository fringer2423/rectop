from django.urls import path

from ..views import rate_info_views as views

app_name = 'Rate info endpoints'
urlpatterns = [
    path('read/<int:pk>', views.read_rate_info, name='read'),
]
