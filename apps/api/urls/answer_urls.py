from django.urls import path

from ..views import answer_views as views

app_name = 'Answer settings endpoints'
urlpatterns = [
    path('create/', views.create_answer),
    path('read/<int:pk>', views.read_answer),
    path('update/<int:pk>', views.update_answer),
    path('delete/<int:pk>', views.delete_answer),
]
