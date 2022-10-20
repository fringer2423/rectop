from django.urls import path

from ..views import rate_views as views

app_name = 'Rate endpoints'
urlpatterns = [
    path('create/', views.create_rate, name='create'),
    path('read/', views.read_rate, name='read'),
    path('update/', views.update_rate, name='update')
]
