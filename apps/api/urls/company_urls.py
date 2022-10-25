from django.urls import path

from ..views import company_views as views

app_name = 'Company endpoints'
urlpatterns = [
    path('create/', views.create_company_view, name='create'),
    path('read/<int:pk>', views.read_company_view, name='read'),
    path('update/<int:pk>', views.update_company_view, name='update'),
    path('delete/<int:pk>', views.delete_company_view, name='delete'),
]
