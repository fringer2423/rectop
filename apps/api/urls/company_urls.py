from django.urls import path

from ..views import company_views as views

app_name = 'Company endpoints'
urlpatterns = [
    path('add/', views.createCompany),
    path('get/<int:pk>', views.getCompany),
    path('update/<int:pk>', views.updateCompany),
]
