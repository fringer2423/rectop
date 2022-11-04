from django.urls import path

from ..views import task_views as views

app_name = 'Task endpoints'
urlpatterns = [
    path('read/<task_id>', views.read_status_task_view, name='read'),
]
