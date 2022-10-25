from django.urls import path

from ..views import answer_views as views

app_name = 'Answer settings endpoints'
urlpatterns = [
    path('create/', views.create_answer_view, name='create'),
    path('read/<int:pk>', views.read_answer_view, name='read'),
    path('update/<int:pk>', views.update_answer_view, name='update'),
    path('delete/<int:pk>', views.delete_answer_view, name='delete'),
]
