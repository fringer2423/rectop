from django.urls import path

from ..views import user_views as views

app_name = 'User endpoints'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('create/', views.register_user),
    path('read/', views.read_user_profile),
    path('update/', views.update_user_profile),
]
