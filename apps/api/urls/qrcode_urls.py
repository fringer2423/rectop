from django.urls import path

from ..views import qrcode_views as views

app_name = 'QRCode endpoints'
urlpatterns = [
    path('create/', views.create_qrcode),
    path('read/<int:pk>', views.read_qrcode),
    path('read/all', views.read_all_qrcodes),
]
