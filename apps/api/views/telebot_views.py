from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import TelebotSerializer

from ..services.telebot_service import create_telebot_by_branch_id_service, get_telebot_by_id_service


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='tg_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Идентификатор Telegram'
        ),
        openapi.Parameter(
            name='branch_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Id branch'
        )
    ],
    responses={
        201: openapi.Response(
            description='Telebot создан',
            schema=TelebotSerializer
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
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает telebot для branch по его {id}, после возвращает информацию о ней.',
    operation_summary='Создать telebot'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_telebot_view(request):
    """Контроллер для создания telebot"""
    user = request.user

    try:
        telebot = create_telebot_by_branch_id_service(
            user=user,
            tg_id=request.data['tg_id'],
            branch_id=request.data['branch_id']
        )
        if telebot:
            serializer = TelebotSerializer(telebot, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такого branch не найдено {e}'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=TelebotSerializer
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
            description='Telebot не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о telebot по {id}.',
    operation_summary='Получить telebot'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_telebot_view(request, pk):
    """Контроллер для отдачи информации о telebot"""
    user = request.user

    try:
        telebot = get_telebot_by_id_service(user, pk)
        if telebot:
            serializer = TelebotSerializer(telebot, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой telebot не найдено {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="put",
    manual_parameters=[
        openapi.Parameter(
            name='tg_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Идентификатор telegram'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=TelebotSerializer
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
    operation_description='Данный endpoint изменяет информацию о telebot по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в изменении.',
    operation_summary='Изменить telebot'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_telebot_view(request, pk):
    """Контроллер для обновления информации telebot"""
    user = request.user
    data = request.data

    try:
        telebot = get_telebot_by_id_service(user, pk)
        if telebot:
            serializer = TelebotSerializer(telebot, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist:
        return Response(data={'detail': 'Такой telebot не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Telebot не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о telebot по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в изменении.',
    operation_summary='Удалить telebot'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_telebot_view(request, pk):
    """Контроллер для удаления информации telebot"""
    user = request.user

    try:
        telebot = get_telebot_by_id_service(user, pk)
        if telebot:
            telebot.delete()
            return Response(data={'detail': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша company'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой telebot не найдено {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
