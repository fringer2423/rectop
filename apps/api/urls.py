from django.urls import re_path, path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Rectop API docs",
        default_version='v0.0.1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('register/', register_user, name='register'),
    path('profile/', getUserProfile, name="users-profile"),
]
