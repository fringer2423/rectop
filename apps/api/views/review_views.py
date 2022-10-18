from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import ReviewSerializer

from ..services.branch_service import get_branch_by_id
from ..services.review_service import create_review_by_branch_id, get_review_by_id, get_all_review_by_company_id


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='full_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Полное имя'
        ),
        openapi.Parameter(
            name='link',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Ссылка'
        ),
        openapi.Parameter(
            name='rating',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Рейтинг'
        ),
        openapi.Parameter(
            name='branch_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Id branch'
        ),
    ],
    responses={
        201: openapi.Response(
            description='Review создан',
            schema=ReviewSerializer
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
    operation_description='Данный endpoint создает review по {id} branch, после возвращает информацию о review.',
    operation_summary='Создать review'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    """Контроллер для создания review"""
    user = request.user

    try:
        review = create_review_by_branch_id(
            user=user,
            branch_id=request.data['branch_id'],
            full_name=request.data['full_name'],
            link=request.data['link'],
            rating=request.data['rating'],
        )
        if review:
            serializer = ReviewSerializer(review, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой branch не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSerializer
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
            description='Review не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о review по {id}.',
    operation_summary='Получить review'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review(request, pk):
    """Контроллер для отдачи информации о review"""
    user = request.user

    try:
        review = get_review_by_id(user=user, review_id=pk)
        if review:
            serializer = ReviewSerializer(review, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой review не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSerializer
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
            description='Branch не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех review по {id} branch.',
    operation_summary='Получить reviews list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_list(request, pk):
    """Контроллер для отдачи информации о всех review branch"""
    user = request.user

    try:
        branch = get_branch_by_id(user=user, branch_id=pk)
        if branch:
            serializer = ReviewSerializer(branch.review_set, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой branch не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="put",
    manual_parameters=[
        openapi.Parameter(
            name='full_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Полное имя'
        ),
        openapi.Parameter(
            name='link',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Ссылка'
        ),
        openapi.Parameter(
            name='rating',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Рейтинг'
        ),
        openapi.Parameter(
            name='status',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Статус заявки'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSerializer
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
            description='review не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о review по {id}. Если владельцем branch является не'
                          ' текущий пользователь, будет отказано в изменении.',
    operation_summary='Изменить review'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review(request, pk):
    """Контроллер для обновления информации review"""
    user = request.user
    data = request.data

    try:
        review = get_review_by_id(user=user, review_id=pk)
        if review:
            serializer = ReviewSerializer(review, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой review не найден'}, status=status.HTTP_404_NOT_FOUND)

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
            description='Branch не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о review по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в удалении.',
    operation_summary='Удалить review'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, pk):
    """Контроллер для удаления информации review"""
    user = request.user

    try:
        review = get_review_by_id(user=user, review_id=pk)
        if review:
            review.delete()
            return Response(data={'detail': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой connect не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=ReviewSerializer
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
    operation_description='Данный endpoint возвращает базовые данные о всех review по {id} company.',
    operation_summary='Получить reviews list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_list_all(request, pk):
    """Контроллер для отдачи информации о всех review компании"""
    user = request.user

    try:
        reviews = get_all_review_by_company_id(user=user, company_id=pk)
        if reviews:
            serializer = ReviewSerializer(reviews, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша company'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой company не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
