from django.urls import path

from ..views import user_views as views

app_name: str = 'User endpoints'
urlpatterns: list = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='login'),
    path('create/', views.register_user_view, name='create'),
    path('read/', views.read_user_profile_view, name='read'),
    path('update/', views.update_user_profile_view, name='update'),
    path('verify/<slug:slug>', views.verify_user_view, name='verify'),
    path('send_code/', views.send_verify_code_user_view, name='send_verify_code'),
    path('verify_code/', views.verify_code_user_view, name='verify_code')
]
