from django.urls import path

from ..views import qrcode_views as views

app_name = 'QRCode endpoints'
urlpatterns = [
    path('create/', views.create_qrcode, name='create'),
    path('read/<int:pk>', views.read_qrcode, name='read'),
    path('read/all', views.read_all_qrcodes, name='read_all'),
]
