import logging
import sys

from logging import Logger

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.core.handlers.wsgi import WSGIRequest
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
from django.http import QueryDict

from ..serializers import BranchSerializer

from ..services.company_services import get_company_by_id_service
from ..services.branch_service import get_branch_by_id_service, create_branch_by_company

from ...core.models import Company, User, Branch

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            name='page',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            required=False,
            description='Страница'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=BranchSerializer
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
    operation_description='Данный endpoint возвращает базовые данные о всех branch по {id} company.',
    operation_summary='Получить branch list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_branch_list_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о branch"""
    user: QuerySet[User] = request.user

    try:
        company: QuerySet[Company] | None = get_company_by_id_service(user, pk)
        if not (company is None):
            branch_list: QuerySet[Branch] = company.branchs.all()
            query: str = request.query_params.get('keyword')
            if query is None:
                query = ''
            page: int = request.query_params.get('page')
            paginator: Paginator = Paginator(branch_list, 10)

            try:
                branch_list = paginator.page(page)
            except PageNotAnInteger:
                branch_list = paginator.page(1)
            except EmptyPage:
                branch_list = paginator.page(paginator.num_pages)

            if page is None:
                page: int = 1

            page = int(page)
            serializer: Serializer[BranchSerializer] = BranchSerializer(branch_list, many=True)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'branches': serializer.data,
                    'page': page,
                    'pages': paginator.num_pages
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
        message = f'Ошибка при обработке запроса {e}'
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
            schema=BranchSerializer
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
    operation_description='Данный endpoint возвращает базовые данные о branch по {id}.',
    operation_summary='Получить branch'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_branch_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о branch"""
    user: QuerySet[User] = request.user

    try:
        branch: QuerySet[Branch] | None = get_branch_by_id_service(user=user, branch_id=pk)
        if not (branch is None):
            serializer: Serializer[BranchSerializer] = BranchSerializer(branch, many=False)
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой branch не найден {e}'
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
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Название филиала'
        ),
        openapi.Parameter(
            name='address',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Адрес'
        ),
        openapi.Parameter(
            name='phone_number',
            in_=openapi.TYPE_NUMBER,
            type=openapi.TYPE_NUMBER,
            required=False,
            description='Номер телефона'
        ),
        openapi.Parameter(
            name='email',
            in_=openapi.FORMAT_EMAIL,
            type=openapi.FORMAT_EMAIL,
            required=False,
            description='Почта'
        ),
        openapi.Parameter(
            name='description',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Описание'
        ),
        openapi.Parameter(
            name='short_description',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Короткое описание'
        ),
        openapi.Parameter(
            name='company_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Company id'
        )
    ],
    responses={
        201: openapi.Response(
            description='Branch создан',
            schema=BranchSerializer
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
            description='Company не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает branch по {id} company, после возвращает информацию'
                          ' о branch.',
    operation_summary='Создать branch'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_branch_view(request: WSGIRequest) -> Response:
    """Контроллер для создания review"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        company_id: int = data['company_id']
        name: str = data['name']
        branch: QuerySet[Branch] | None = create_branch_by_company(user=user, name=name, company_id=company_id)
        if not (branch is None):
            serializer: Serializer[BranchSerializer] = BranchSerializer(branch, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            message: str = 'Это не ваш company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
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

    except ObjectDoesNotExist as e:
        message: str = f'Такой company не найден {e}'
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
            description='Название филиала'
        ),
        openapi.Parameter(
            name='address',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Адрес'
        ),
        openapi.Parameter(
            name='phone_number',
            in_=openapi.TYPE_NUMBER,
            type=openapi.TYPE_NUMBER,
            required=False,
            description='Номер телефона'
        ),
        openapi.Parameter(
            name='email',
            in_=openapi.FORMAT_EMAIL,
            type=openapi.FORMAT_EMAIL,
            required=False,
            description='Почта'
        ),
        openapi.Parameter(
            name='description',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Описание'
        ),
        openapi.Parameter(
            name='short_description',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Короткое описание'
        ),
    ],
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=BranchSerializer
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
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint изменяет информацию о branch по {id}. Если владельцем branch является не'
                          ' текущий пользователь, будет отказано в изменении. Можно изменять не все поля.',
    operation_summary='Изменить branch'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_branch_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для обновления информации branch"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data

    try:
        branch: QuerySet[Branch] | None = get_branch_by_id_service(user, pk)
        if not (branch is None):
            serializer: Serializer[BranchSerializer] = BranchSerializer(branch, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message: str = f'Такой branch не найден {e}'
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
