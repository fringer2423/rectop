import logging
import sys

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from ..serializers import AnswerSerializer

from ..services.answer_service import get_answer_by_id_service, create_answer_by_review_id_service
from ...core.models import Answer, User

logger: logging.Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип answer'
        ),
        openapi.Parameter(
            name='body',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тело answer'
        ),
        openapi.Parameter(
            name='review_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Id review'
        ),
    ],
    responses={
        201: openapi.Response(
            description='Answer создан',
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
            description='Review не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        406: openapi.Response(
            description='Answer уже создан для этого review'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает answer по {id} review, после возвращает информацию о answer.',
    operation_summary='Создать answer'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_answer_view(request: WSGIRequest) -> Response:
    """Контроллер для создания answer"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        answer: QuerySet[Answer] | None = create_answer_by_review_id_service(
            user=user,
            review_id=data['review_id'],
            body=data['body'],
            type_answer=data['type'],
        )
        if not(answer is None):
            serializer: Serializer[AnswerSerializer] = AnswerSerializer(answer, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            message: str = 'Это не ваш review'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой review не найден {e}'
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
                'detail':
                    message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except IntegrityError as e:
        message: str = f'Answer уже создан для этого review {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_406_NOT_ACCEPTABLE
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
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о answer по {id}.',
    operation_summary='Получить answer'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_answer_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о answer"""
    user: QuerySet[User] = request.user

    try:
        answer: QuerySet[Answer] | None = get_answer_by_id_service(user=user, answer_id=pk)
        if not(answer is None):
            serializer: Serializer[AnswerSerializer] = AnswerSerializer(answer, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваш answer'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой answer не найден {e}'
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
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тип answer'
        ),
        openapi.Parameter(
            name='body',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Тело answer'
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
            description='Answer не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о answer по {id}. Если у пользователя нет прав на'
                          ' изменение отзыва, будет отказано в изменении.',
    operation_summary='Изменить answer'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_answer_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для обновления информации answer"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        answer: QuerySet[Answer] | None = get_answer_by_id_service(user=user, answer_id=pk)
        if not(answer is None):
            serializer: Serializer[AnswerSerializer] = AnswerSerializer(answer, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваш answer'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой answer не найден {e}'
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
            description='Answer не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о answer по {id}. Если владельцем компании является не'
                          ' текущий пользователь, будет отказано в удалении.',
    operation_summary='Удалить answer'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_answer_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для удаления информации answer"""
    user: QuerySet[User] = request.user

    try:
        answer: QuerySet[Answer] | None = get_answer_by_id_service(user=user, answer_id=pk)
        if not(answer is None):
            answer.delete()
            message: str = 'Удаление выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваш answer'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой answer не найден {e}'
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
