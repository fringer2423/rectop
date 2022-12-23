import logging
import sys

from logging import Logger

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from ..serializers import RateSerializer

from ...core.models import User, Rate

from ..services.rate_service import get_rate_by_user_service, create_rate_by_user_service

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип rate'
        ),
    ],
    responses={
        201: openapi.Response(
            description='Rate создан',
            schema=RateSerializer
        ),
        400: openapi.Response(
            description='Ошибка при создании'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        403: openapi.Response(
            description='Ошибка доступа'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        406: openapi.Response(
            description='Rate уже создан для этого user'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает rate по user, после возвращает информацию о rate.',
    operation_summary='Создать rate'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rate_view(request: WSGIRequest) -> Response:
    """Контроллер для создания rate"""
    user: QuerySet[User] = request.user

    try:
        rate: QuerySet[Rate] | None = create_rate_by_user_service(
            user=user,
        )
        serializer: Serializer[RateSerializer] = RateSerializer(rate, many=False)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    except KeyError as e:
        message: str = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except IntegrityError as e:
        message: str = f'Rate уже создан для этого user {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    except Exception as e:
        message: str = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=RateSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        403: openapi.Response(
            description='Ошибка доступа'
        ),
        404: openapi.Response(
            description='Rate не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о rate.',
    operation_summary='Получить rate'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_rate_view(request: WSGIRequest) -> Response:
    """Контроллер для отдачи информации о rate"""
    user: QuerySet[User] = request.user

    try:
        rate: QuerySet[Rate] | None = get_rate_by_user_service(user=user)
        serializer: Serializer[RateSerializer] = RateSerializer(rate, many=False)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist as e:
        message: str = f'Такой rate не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message: str = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@swagger_auto_schema(
    method="put",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип rate'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=RateSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        403: openapi.Response(
            description='Ошибка доступа'
        ),
        404: openapi.Response(
            description='Rate не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о rate.',
    operation_summary='Изменить rate'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_rate_view(request: WSGIRequest) -> Response:
    """Контроллер для обновления информации rate"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data
    try:
        rate: QuerySet[Rate] | None = get_rate_by_user_service(user=user)
        serializer: Serializer[RateSerializer] = RateSerializer(rate, many=False, partial=True, data=data)
        if serializer.is_valid():
            serializer.save()
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist as e:
        message: str = f'Такой rate не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError as e:
        message: str = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except Exception as e:
        message: str = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )
