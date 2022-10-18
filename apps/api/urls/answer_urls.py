from django.urls import path

from ..views import answer_views as views

app_name = 'Answer settings endpoints'
urlpatterns = [
    path('create/', views.create_answer, name='create'),
    path('read/<int:pk>', views.read_answer, name='read'),
    path('update/<int:pk>', views.update_answer, name='update'),
    path('delete/<int:pk>', views.delete_answer, name='delete'),
]
