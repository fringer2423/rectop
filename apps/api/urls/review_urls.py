from django.urls import path

from ..views import review_views as views

app_name = 'Connect endpoints'
urlpatterns = [
    path('create/', views.create_review),
    path('read/<int:pk>', views.read_review),
    path('read/list/<int:pk>', views.read_review_list),
    path('read/list/all/<int:pk>', views.read_review_list_all),
    path('update/<int:pk>', views.update_review),
    path('delete/<int:pk>', views.delete_review),
]
