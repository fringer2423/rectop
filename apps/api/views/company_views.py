import logging
import sys

from logging import Logger

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

from ..serializers import CompanySerializer

from ..services.company_services import get_company_by_id_service, create_company_by_company_name_service
from ...core.models import Company, User

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Название'
        )
    ],
    responses={
        201: openapi.Response(
            description='Company успешно создана',
            schema=CompanySerializer
        ),
        400: openapi.Response(
            description='Ошибка при создании'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает company, после возвращает информацию о ней. Поле owner показывает'
                          ' данные владельца.',
    operation_summary='Создать company'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_company_view(request: WSGIRequest) -> Response:
    """Контроллер для создания company"""
    user: QuerySet[User] = request.user

    try:
        company: QuerySet[Company] | None = create_company_by_company_name_service(user, request.data['name'])
        serializer: Serializer[CompanySerializer] = CompanySerializer(company, many=False)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
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
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
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
            schema=CompanySerializer
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
    operation_description='Данный endpoint возвращает базовые данные о company по {id}. Поле owner показывает данные'
                          ' владельца.',
    operation_summary='Получить company'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_company_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о company"""
    user: QuerySet[User] = request.user

    try:
        company: QuerySet[Company] | None = get_company_by_id_service(user, pk)
        if not(company is None):
            serializer: Serializer[CompanySerializer] = CompanySerializer(company, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой company не найдено {e}'
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
            name='name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Название')
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=CompanySerializer
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
    operation_description='Данный endpoint изменяет информацию о company по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в изменении. Поле owner показывает данные '
                          'владельца.',
    operation_summary='Изменить company'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_company_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для обновления информации company"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        company: QuerySet[Company] | None = get_company_by_id_service(user, pk)
        if not(company is None):
            serializer: Serializer[CompanySerializer] = CompanySerializer(company, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
                message: str = 'Запрос выполнен успешно'
                logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist:
        message: str = 'Такой company не найдено'
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
            description='Company не найдена'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint удаляет информацию о company по {id}. Если владельцем company является не'
                          ' текущий пользователь, будет отказано в изменении. Поле owner показывает данные '
                          'владельца.',
    operation_summary='Удалить company'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_company_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для удаления информации company"""
    user: QuerySet[User] = request.user

    try:
        company: QuerySet[Company] | None= get_company_by_id_service(user, pk)
        if not(company is None):
            company.delete()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой company не найдено {e}'
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
