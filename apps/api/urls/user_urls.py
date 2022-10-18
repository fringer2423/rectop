from django.urls import path

from ..views import user_views as views

app_name = 'User endpoints'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('create/', views.register_user, name='create'),
    path('read/', views.read_user_profile, name='read'),
    path('update/', views.update_user_profile, name='update'),
]
