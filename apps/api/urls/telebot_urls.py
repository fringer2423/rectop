from django.urls import path

from ..views import telebot_views as views

app_name = 'Telebot endpoints'
urlpatterns = [
    path('create/', views.create_telebot),
    path('read/<int:pk>', views.read_telebot),
    path('update/<int:pk>', views.update_telebot),
    path('delete/<int:pk>', views.delete_telebot),
]