from django.urls import path

from ..views import user_views as views

app_name = 'user endpoints'
urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('create/', views.register_user),
    path('read/', views.getUserProfile),
    path('update/', views.updateUserProfile),
]
