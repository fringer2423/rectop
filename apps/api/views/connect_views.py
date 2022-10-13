from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import ConnectSerializer

from ..services.connect_service import create_connect_by_company_id, get_connect_by_id
from ..services.company_services import get_company_by_id


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
            description='Id компании'
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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint создает connect по {id} компании, после возвращает информацию о connect.',
    operation_summary='Создать connect'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_connect(request):
    """
    Контроллер для создания connect
    :param pk: id компании
    :param request:
    :return: response
    """
    user = request.user

    try:
        company_id = request.data['company_id']
        connect = create_connect_by_company_id(
            user=user,
            connect_type=request.data['type'],
            key=request.data['key'],
            company_id=company_id
        )
        if connect:
            serializer = ConnectSerializer(connect, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о connect по {id}.',
    operation_summary='Получить информацию о connect'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_connect(request, pk):
    """Контроллер для отдачи информации о connect"""
    user = request.user

    try:
        telebot = get_connect_by_id(user=user, connect_id=pk)
        if telebot:
            serializer = ConnectSerializer(telebot, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой connect не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех connect по {id} компании.',
    operation_summary='Получить информацию о connects по id компании'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_connect_list(request, pk):
    """Контроллер для отдачи информации о всех connect компании"""
    user = request.user

    try:
        company = get_company_by_id(user=user, company_id=pk)
        if company:
            serializer = ConnectSerializer(company.connect_set, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint изменяет информацию о connect по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в изменении. Можно изменять не все поля.',
    operation_summary='Изменить информацию о connect'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_connect(request, pk):
    """Контроллер для обновления информации connect"""
    user = request.user
    data = request.data

    try:
        connect = get_connect_by_id(user, pk)
        if connect:
            serializer = ConnectSerializer(connect, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой connect не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint удаляет информацию о connect по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в удалении.',
    operation_summary='Удалить информацию о connect'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_connect(request, pk):
    """Контроллер для удаления информации connect"""
    user = request.user

    try:
        connect = get_connect_by_id(user, pk)
        if connect:
            connect.delete()
            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой connect не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
