from django.urls import path

from ..views import branch_views as views

app_name = 'Branchs endpoints'
urlpatterns = [
    path('read/list/<int:pk>', views.read_branch_list),
    path('read/<int:pk>', views.read_branch),
]
