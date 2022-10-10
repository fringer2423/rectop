from django.urls import path

from ..views import user_views as views

app_name = 'user endpoints'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('register/', views.register_user),
    path('profile/', views.getUserProfile),
    path('edit/', views.updateUserProfile),
]
