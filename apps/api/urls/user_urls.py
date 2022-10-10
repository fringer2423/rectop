from django.urls import path

from ..views import user_views as views

app_name = 'user endpoints'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('register/', views.register_user, name='register'),
    path('profile/', views.getUserProfile, name="users-profile"),
]
