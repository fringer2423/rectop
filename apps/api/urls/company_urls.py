from django.urls import path

from ..views import company_views as views

app_name = 'Company endpoints'
urlpatterns = [
    path('create/', views.create_company, name='create'),
    path('read/<int:pk>', views.read_company, name='read'),
    path('update/<int:pk>', views.update_company, name='update'),
    path('delete/<int:pk>', views.delete_company, name='delete'),
]
