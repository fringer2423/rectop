from django.urls import path

from ..views import rate_views as views

app_name: str = 'Rate endpoints'
urlpatterns: list = [
    path('create/', views.create_rate_view, name='create'),
    path('read/', views.read_rate_view, name='read'),
    path('update/', views.update_rate_view, name='update')
]
