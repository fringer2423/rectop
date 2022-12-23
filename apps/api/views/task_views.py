import logging
import sys

from logging import Logger

from django.core.handlers.wsgi import WSGIRequest
from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from celery.result import AsyncResult

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..serializers import TaskSerializer

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос прошел успешно',
            schema=TaskSerializer
        ),
        400: openapi.Response(
            description='Ошибка при обработке запроса'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        404: openapi.Response(
            description='Task не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
    },
    operation_description='Данный endpoint возвращает информацию о task',
    operation_summary='Получить task'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_status_task_view(request: WSGIRequest, task_id: int) -> Response:
    task_result: QueryDict = AsyncResult(task_id)
    serializer: Serializer[TaskSerializer] = TaskSerializer(task_result)
    message: str = 'Запрос выполнен успешно'
    logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )
