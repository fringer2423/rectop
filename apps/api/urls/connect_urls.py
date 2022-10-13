from django.urls import path

from ..views import connect_views as views

app_name = 'Connect endpoints'
urlpatterns = [
    path('create/', views.create_connect),
    path('read/<int:pk>', views.read_connect),
    path('read/list/<int:pk>', views.read_connect_list),
    path('update/<int:pk>', views.update_connect),
    path('delete/<int:pk>', views.delete_connect),
]
