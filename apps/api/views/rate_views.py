from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from ..serializers import RateSerializer

from ..services.rate_service import get_rate_by_user_service, create_rate_by_user_service


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
def create_rate_view(request):
    """Контроллер для создания rate"""
    user = request.user

    try:
        rate = create_rate_by_user_service(
            user=user,
        )
        serializer = RateSerializer(rate, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except IntegrityError as e:
        return Response(data={'detail': 'Rate уже создан для этого user'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def read_rate_view(request):
    """Контроллер для отдачи информации о rate"""
    user = request.user

    try:
        rate = get_rate_by_user_service(user=user)
        serializer = RateSerializer(rate, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой rate не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def update_rate_view(request):
    """Контроллер для обновления информации rate"""
    user = request.user
    data = request.data
    try:
        rate = get_rate_by_user_service(user=user)
        serializer = RateSerializer(rate, many=False, partial=True, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой rate не найден'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
