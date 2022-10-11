from django.urls import path

from ..views import company_views as views

app_name = 'Company endpoints'
urlpatterns = [
    path('create/', views.createCompany),
    path('read/<int:pk>', views.getCompany),
    path('update/<int:pk>', views.updateCompany),
    path('delete/<int:pk>', views.deleteCompany),
]
