from django.urls import path

from ..views import connect_views as views

app_name: str = 'Connect endpoints'
urlpatterns: list = [
    path('create/', views.create_connect_view, name='create'),
    path('read/<int:pk>', views.read_connect_view, name='read'),
    path('read/list/<int:pk>', views.read_connect_list_view, name='read_list'),
    path('update/<int:pk>', views.update_connect_view, name='update'),
    path('delete/<int:pk>', views.delete_connect_view, name='delete'),
]
