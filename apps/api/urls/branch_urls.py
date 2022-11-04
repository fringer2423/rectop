from django.urls import path

from ..views import branch_views as views

app_name = 'Branchs endpoints'
urlpatterns = [
    path('read/list/<int:pk>', views.read_branch_list_view, name='read_list'),
    path('read/<int:pk>', views.read_branch_view, name='read'),
    path('create/', views.create_branch_view, name='create'),
    path('update/<int:pk>', views.update_branch_view, name='update')
]
