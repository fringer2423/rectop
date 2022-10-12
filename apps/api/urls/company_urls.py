from django.urls import path

from ..views import company_views as views

app_name = 'Company endpoints'
urlpatterns = [
    path('create/', views.create_company),
    path('read/<int:pk>', views.read_company),
    path('update/<int:pk>', views.update_company),
    path('delete/<int:pk>', views.delete_company),
]
