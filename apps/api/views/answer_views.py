from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import AnswerSerializer

from ..services.answer_service import get_answer_by_id, create_answer_by_review_id


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип отзыва'
        ),
        openapi.Parameter(
            name='body',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тело ответа'
        ),
        openapi.Parameter(
            name='review_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Id отзыва'
        ),
    ],
    responses={
        201: openapi.Response(
            description='Review создан',
            schema=AnswerSerializer
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
            description='Отзыв не найден'
        )
    },
    operation_description='Данный endpoint создает answer по {id} отзыва, после возвращает информацию о answer.',
    operation_summary='Создать answer'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_answer(request):
    """
    Контроллер для создания answer
    :param request:
    :return: response
    """
    user = request.user

    try:
        answer = create_answer_by_review_id(
            user=user,
            review_id=request.data['review_id'],
            body=request.data['body'],
            type=request.data['type'],
        )
        if answer:
            serializer = AnswerSerializer(answer, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш отзыв'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой отзыв не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=AnswerSerializer
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
            description='answer не найден'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о answer по {id}.',
    operation_summary='Получить информацию о answer'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_answer(request, pk):
    """Контроллер для отдачи информации о answer"""
    user = request.user

    try:
        answer = get_answer_by_id(user=user, answer_id=pk)
        if answer:
            serializer = AnswerSerializer(answer, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш ответ'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой ответ не найден'}, status=status.HTTP_404_NOT_FOUND)

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
            description='Тип отзыва'
        ),
        openapi.Parameter(
            name='body',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тело ответа'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=AnswerSerializer
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
            description='answer не найден'
        )
    },
    operation_description='Данный endpoint изменяет информацию о answer по {id}. Если владельцем филиала является не'
                          ' авторизованный пользователь, будет отказано в изменении.',
    operation_summary='Изменить информацию о answer'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_answer(request, pk):
    """Контроллер для обновления информации answer"""
    user = request.user
    data = request.data

    try:
        answer = get_answer_by_id(user=user, answer_id=pk)
        if answer:
            serializer = AnswerSerializer(answer, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш ответ'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой answer не найден'}, status=status.HTTP_404_NOT_FOUND)

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
            description='Ответ не найден'
        )
    },
    operation_description='Данный endpoint удаляет информацию о answer по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в удалении.',
    operation_summary='Удалить информацию о answer'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_answer(request, pk):
    """Контроллер для удаления информации answer"""
    user = request.user

    try:
        answer = get_answer_by_id(user=user, answer_id=pk)
        if answer:
            answer.delete()
            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваш answer'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой answer не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
