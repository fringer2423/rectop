import logging
import sys

from logging import Logger

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import QueryDict

from ..serializers import ReviewSettingsSerializer

from ...core.models import User, ReviewSettings

from ..services.review_settings_service import get_review_settings_by_id_service, \
    create_review_settings_by_company_id_service

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='company_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='id company'
        ),
        openapi.Parameter(
            name='mask',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Настройка автоответа на отзывы'
        )
    ],
    responses={
        201: openapi.Response(
            description='Review settings создан',
            schema=ReviewSettingsSerializer
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
        404: openapi.Response(
            description='Company не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает review settings по {id} company, после возвращает информацию о'
                          ' review settings.',
    operation_summary='Создать review settings'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review_settings_view(request: WSGIRequest) -> Response:
    """Контроллер для создания review settings """
    user: QuerySet[User] = request.user

    try:
        company_id: int = request.data['company_id']
        review_settings: QuerySet[ReviewSettings] | None = create_review_settings_by_company_id_service(
            user=user,
            mask=request.data['mask'],
            company_id=company_id
        )
        if not (review_settings is None):
            serializer: Serializer[ReviewSettingsSerializer] = ReviewSettingsSerializer(review_settings, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой company не найдено {e}'
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


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSettingsSerializer
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
            description='Company не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о review settings по {id}.',
    operation_summary='Получить review settings'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_settings_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о review settings"""
    user: QuerySet[User] = request.user

    try:
        review_settings: QuerySet[ReviewSettings] | None = get_review_settings_by_id_service(
            user=user,
            review_settings_id=pk
        )
        if not (review_settings is None):
            serializer: Serializer[ReviewSettingsSerializer] = ReviewSettingsSerializer(review_settings, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой review settings не найден {e}'
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
            name='mask',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Настройка автоответов на отзывы'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSettingsSerializer
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
            description='Company не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о review settings по {id}. Если владельцем company '
                          'является не текущий пользователь, будет отказано в изменении. Можно изменять не все '
                          'поля.',
    operation_summary='Изменить review settings'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review_settings_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для обновления информации review settings"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        review_settings: QuerySet[ReviewSettings] | None = get_review_settings_by_id_service(user, pk)
        if not (review_settings is None):
            serializer: Serializer[ReviewSettingsSerializer] = ReviewSettingsSerializer(
                review_settings,
                many=False,
                partial=True,
                data=data
            )
            if serializer.is_valid():
                serializer.save()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой review settings не найден {e}'
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


@swagger_auto_schema(
    method="delete",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно'
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
            description='Company не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о connect по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в удалении.',
    operation_summary='Удалить review settings'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review_settings_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для удаления информации review settings"""
    user: QuerySet[User] = request.user

    try:
        review_settings: QuerySet[ReviewSettings] | None = get_review_settings_by_id_service(user, pk)
        if not (review_settings is None):
            review_settings.delete()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой review settings не найден {e}'
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
