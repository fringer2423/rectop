from django.urls import path

from ..views import rate_info_views as views

app_name: str = 'Rate info endpoints'
urlpatterns: list = [
    path('read/', views.read_rate_info_view, name='read'),
]
