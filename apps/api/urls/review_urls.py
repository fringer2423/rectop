from django.urls import path

from ..views import review_views as views

app_name: str = 'Connect endpoints'
urlpatterns: list = [
    path('create/', views.create_review_view, name='create'),
    path('read/<int:pk>', views.read_review_view, name='read'),
    path('read/list/<int:pk>', views.read_review_list_view, name='read_list'),
    path('read/list/all/<int:pk>', views.read_review_list_all_view, name='read_all'),
    path('update/<int:pk>', views.update_review_view, name='update'),
    path('delete/<int:pk>', views.delete_review_view, name='delete'),
]
