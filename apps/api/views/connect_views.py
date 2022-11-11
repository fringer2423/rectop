import logging
import sys

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from ..serializers import ConnectSerializer

from ..services.connect_service import create_connect_by_branch_id_service, get_connect_by_id_service
from ..services.branch_service import get_branch_by_id_service

logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип платформы подключения'
        ),
        openapi.Parameter(
            name='key',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Ключ для подключения'
        ),
        openapi.Parameter(
            name='company_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Id branch'
        )
    ],
    responses={
        201: openapi.Response(
            description='Connect создан',
            schema=ConnectSerializer
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
            description='Branch не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        406: openapi.Response(
            description='Connect уже создан для этого branch'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает connect по {id} branch, после возвращает информацию о connect.',
    operation_summary='Создать connect'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_connect_view(request):
    """Контроллер для создания connect"""
    user = request.user

    try:
        branch_id = request.data['branch_id']
        connect = create_connect_by_branch_id_service(
            user=user,
            connect_type=request.data['type'],
            key=request.data['key'],
            branch_id=branch_id
        )
        if connect:
            serializer = ConnectSerializer(connect, many=False)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найдено {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except IntegrityError as e:
        message = f'QRCode уже создан для этого branch {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
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
            schema=ConnectSerializer
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
            description='Connect не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о connect по {id}.',
    operation_summary='Получить connect'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_connect_view(request, pk):
    """Контроллер для отдачи информации о connect"""
    user = request.user

    try:
        telebot = get_connect_by_id_service(user=user, connect_id=pk)
        if telebot:
            serializer = ConnectSerializer(telebot, many=False)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваша branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой connect не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
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
            schema=ConnectSerializer
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
    operation_description='Данный endpoint возвращает базовые данные о всех connect по {id} branch.',
    operation_summary='Получить connects list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_connect_list_view(request, pk):
    """Контроллер для отдачи информации о всех connect company"""
    user = request.user

    try:
        branch = get_branch_by_id_service(user=user, branch_id=pk)
        if branch:
            serializer = ConnectSerializer(branch.connect_set, many=True)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найдено {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
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
            description='Тип платформы подключения'
        ),
        openapi.Parameter(
            name='key',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Ключ для подключения'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ConnectSerializer
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
            description='Connect не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о connect по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в изменении. Можно изменять не все поля.',
    operation_summary='Изменить connect'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_connect_view(request, pk):
    """Контроллер для обновления информации connect"""
    user = request.user
    data = request.data

    try:
        connect = get_connect_by_id_service(user, pk)
        if connect:
            serializer = ConnectSerializer(connect, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой connect не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
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
            description='Connect не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о connect по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в удалении.',
    operation_summary='Удалить connect'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_connect_view(request, pk):
    """Контроллер для удаления информации connect"""
    user = request.user

    try:
        connect = get_connect_by_id_service(user, pk)
        if connect:
            connect.delete()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой connect не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )
