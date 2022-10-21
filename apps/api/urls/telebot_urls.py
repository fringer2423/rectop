from django.urls import path

from ..views import telebot_views as views

app_name = 'Telebot endpoints'
urlpatterns = [
    path('create/', views.create_telebot_view, name='create'),
    path('read/<int:pk>', views.read_telebot_view, name='read'),
    path('update/<int:pk>', views.update_telebot_view, name='update'),
    path('delete/<int:pk>', views.delete_telebot_view, name='delete'),
]
