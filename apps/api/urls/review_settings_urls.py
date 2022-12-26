from django.urls import path

from ..views import review_settings_views as views

app_name: str = 'Review settings endpoints'
urlpatterns: list = [
    path('create/', views.create_review_settings_view, name='create'),
    path('read/<int:pk>', views.read_review_settings_view, name='read'),
    path('update/<int:pk>', views.update_review_settings_view, name='update'),
    path('delete/<int:pk>', views.delete_review_settings_view, name='delete'),
]
