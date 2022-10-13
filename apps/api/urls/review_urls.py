from django.urls import path

from ..views import review_views as views

app_name = 'Connect endpoints'
urlpatterns = [
    path('create/<int:pk>', views.create_review),
    path('read/<int:pk>', views.read_review),
    path('read/list/<int:pk>', views.read_review_list),
    path('update/<int:pk>', views.update_review),
    path('delete/<int:pk>', views.delete_review),
]
