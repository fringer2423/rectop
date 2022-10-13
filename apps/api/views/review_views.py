from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import ReviewSerializer

from ..services.branch_service import get_branch_by_branch_id
from ..services.review_service import create_review_by_branch_id, get_review_by_id


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
            description='Id филиала'
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
            description='Филиал не найден'
        )
    },
    operation_description='Данный endpoint создает review по {id} филиала, после возвращает информацию о review.',
    operation_summary='Создать review'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    """
    Контроллер для создания review
    :param pk: id филиала
    :param request:
    :return: response
    """
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
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой филиал не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при создании ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='review не найден'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о review по {id}.',
    operation_summary='Получить информацию о review'
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
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой review не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при создании ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Филиал не найден'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех review по {id} филиала.',
    operation_summary='Получить информацию о reviews по id филиала'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_list(request, pk):
    """Контроллер для отдачи информации о всех review филиала"""
    user = request.user

    try:
        branch = get_branch_by_branch_id(user=user, branch_id=pk)
        if branch:
            serializer = ReviewSerializer(branch.review_set, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой филиал не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при создании ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
        )
    },
    operation_description='Данный endpoint изменяет информацию о review по {id}. Если владельцем филиала является не'
                          ' авторизованный пользователь, будет отказано в изменении.',
    operation_summary='Изменить информацию о review'
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
            return Response(data={'message': 'Это не ваш филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой review не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при создании ' + e.__str__()
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
            description='Филиал не найден'
        )
    },
    operation_description='Данный endpoint удаляет информацию о review по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в удалении.',
    operation_summary='Удалить информацию о review'
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
            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой connect не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при создании ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
