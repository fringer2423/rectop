from django.urls import path

from ..views import review_views as views

app_name = 'Connect endpoints'
urlpatterns = [
    path('create/', views.create_review, name='create'),
    path('read/<int:pk>', views.read_review, name='read'),
    path('read/list/<int:pk>', views.read_review_list, name='read_list'),
    path('read/list/all/<int:pk>', views.read_review_list_all, name='read_all'),
    path('update/<int:pk>', views.update_review, name='update'),
    path('delete/<int:pk>', views.delete_review, name='delete'),
]
