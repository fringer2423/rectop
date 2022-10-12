from django.urls import path

from ..views import telebot_views as views

app_name = 'Telebot endpoints'
urlpatterns = [
    path('create/<int:pk>', views.createTelebot),
    path('read/<int:pk>', views.getTelebot),
    path('update/<int:pk>', views.updateTelebot),
    path('delete/<int:pk>', views.deleteTelebot),
]
