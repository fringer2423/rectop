from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import ReviewSettingsSerializer

from ..services.review_settings_service import get_review_settings_by_id, create_review_settings_by_company_id


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='company_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='id компании'
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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint создает review settings по {id} компании, после возвращает информацию о'
                          ' review settings.',
    operation_summary='Создать review settings'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review_settings(request):
    """
    Контроллер для создания review settings
    :param request:
    :return: response
    """
    user = request.user

    try:
        company_id = request.data['company_id']
        review_settings = create_review_settings_by_company_id(
            user=user,
            mask=request.data['mask'],
            company_id=company_id
        )
        if review_settings:
            serializer = ReviewSettingsSerializer(review_settings, many=False)
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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о review settings по {id}.',
    operation_summary='Получить информацию о review settings'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_settings(request, pk):
    """Контроллер для отдачи информации о review settings"""
    user = request.user

    try:
        review_settings = get_review_settings_by_id(user=user, review_settings_id=pk)
        if review_settings:
            serializer = ReviewSettingsSerializer(review_settings, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой review settings не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint изменяет информацию о review settings по {id}. Если владельцем компании '
                          'является не авторизованный пользователь, будет отказано в изменении. Можно изменять не все '
                          'поля.',
    operation_summary='Изменить информацию о review settings'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review_settings(request, pk):
    """Контроллер для обновления информации review settings"""
    user = request.user
    data = request.data

    try:
        review_settings = get_review_settings_by_id(user, pk)
        if review_settings:
            serializer = ReviewSettingsSerializer(review_settings, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой review settings не найден'}, status=status.HTTP_404_NOT_FOUND)

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
def delete_review_settings(request, pk):
    """Контроллер для удаления информации review settings"""
    user = request.user

    try:
        review_settings = get_review_settings_by_id(user, pk)
        if review_settings:
            review_settings.delete()
            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой review_settings не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
