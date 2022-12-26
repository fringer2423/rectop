from django.urls import path

from ..views import qrcode_views as views

app_name: str = 'QRCode endpoints'
urlpatterns: list = [
    path('create/', views.create_qrcode_view, name='create'),
    path('read/<int:pk>', views.read_qrcode_view, name='read'),
    path('read/all', views.read_all_qrcodes_view, name='read_all'),
]
