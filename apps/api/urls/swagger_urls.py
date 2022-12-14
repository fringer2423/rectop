from django.urls import re_path

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view: object = get_schema_view(
    openapi.Info(
        title='RecTop API docs',
        description='Документация к API RecTop',
        default_version='v0.1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

app_name: str = 'swagger'
urlpatterns: list = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
