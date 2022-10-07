from django.urls import path

from ..views import user_views as views

app_name = 'api_v0.0.1'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('register/', views.register_user, name='register'),
    path('profile/', views.getUserProfile, name="users-profile"),
]
