from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import TelebotSerializer

from ..services.telebot_service import create_telebot_by_branch_id, get_telebot_by_id


@swagger_auto_schema(
    method="post",
    manual_parameters=[openapi.Parameter('tg_id', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True,
                                         description='Идентификатор Telegram')],
    responses={201: openapi.Response(description='Telebot создан', schema=TelebotSerializer),
               400: openapi.Response(description='Ошибка при создании'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Филиал не найден')},
    operation_description='Данный endpoint создает telebot для филиала по его {id}, после возвращает информацию о ней.',
    operation_summary='Создать telebot'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_telebot(request, pk):
    """
    Контроллер для создания telebot
    :param pk: id филиала
    :param request:
    :return: response
    """
    user = request.user
    print(pk)

    try:
        telebot = create_telebot_by_branch_id(user=user, tg_id=request.data['tg_id'], branch_id=pk)
        if telebot:
            serializer = TelebotSerializer(telebot, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такого филиала не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as er:
        message = f'Ошибка при создании {er}'
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={200: openapi.Response(description='Запрос выполнен успешно', schema=TelebotSerializer),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Компания не найдена')},
    operation_description='Данный endpoint возвращает базовые данные о telebot по {id}.',
    operation_summary='Получить информацию о telebot'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_telebot(request, pk):
    """Контроллер для отдачи информации о telebot"""
    user = request.user

    try:
        telebot = get_telebot_by_id(user, pk)
        if telebot:
            serializer = TelebotSerializer(telebot, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой telebot не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return Response(data={'message': 'Ошибка при запросе'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="put",
    manual_parameters=[openapi.Parameter('tg_id', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True,
                                         description='Идентификатор telegram')],
    responses={200: openapi.Response(description='Запрос выполнен успешно', schema=TelebotSerializer),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Компания не найдена')},
    operation_description='Данный endpoint изменяет информацию о telebot по {id}. Если владельцем филиала является не'
                          ' авторизованный пользователь, будет отказано в изменении.',
    operation_summary='Изменить информацию о telebot'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_telebot(request, pk):
    """Контроллер для обновления информации telebot"""
    user = request.user

    try:
        telebot = get_telebot_by_id(user, pk)

        if telebot:
            telebot.tg_id = request.data['tg_id']
            telebot.save()

            serializer = TelebotSerializer(telebot, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой telebot не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return Response(data={'message': 'Ошибка при запросе '}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="delete",
    responses={200: openapi.Response(description='Запрос выполнен успешно'),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Компания не найдена')},
    operation_description='Данный endpoint удаляет информацию о telebot по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в изменении.',
    operation_summary='Удалить информацию о telebot'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_telebot(request, pk):
    """Контроллер для удаления информации telebot"""
    user = request.user

    try:
        telebot = get_telebot_by_id(user, pk)

        if telebot:
            telebot.delete()

            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой telebot не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return Response(data={'message': 'Ошибка при запросе '}, status=status.HTTP_400_BAD_REQUEST)
