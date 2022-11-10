import logging
import sys

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..serializers import BranchSerializer

from ..services.company_services import get_company_by_id_service
from ..services.branch_service import get_branch_by_id_service, create_branch_by_company

logger = logging.getLogger('django')


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
    operation_description='Данный endpoint возвращает базовые данные о всех branch по {id} company.',
    operation_summary='Получить branch list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_branch_list_view(request, pk):
    """Контроллер для отдачи информации о branch"""
    user = request.user

    try:
        company = get_company_by_id_service(user, pk)
        if company:
            branch_list = company.branchs.all()
            query = request.query_params.get('keyword')
            if query is None:
                query = ''
            page = request.query_params.get('page')
            paginator = Paginator(branch_list, 10)

            try:
                branch_list = paginator.page(page)
            except PageNotAnInteger:
                branch_list = paginator.page(1)
            except EmptyPage:
                branch_list = paginator.page(paginator.num_pages)

            if page is None:
                page = 1

            page = int(page)
            serializer = BranchSerializer(branch_list, many=True)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'reviews': serializer.data,
                    'page': page,
                    'pages': paginator.num_pages
                },
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data={'detail': message}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        message = f'Такой company не найдено {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def read_branch_view(request, pk):
    """Контроллер для отдачи информации о branch"""
    user = request.user

    try:
        branch = get_branch_by_id_service(user=user, branch_id=pk)
        if branch:
            serializer = BranchSerializer(branch, many=False)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data={'detail': message}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def create_branch_view(request):
    """Контроллер для создания review"""
    user = request.user

    try:
        company_id = request.data['company_id']
        name = request.data['name']
        branch = create_branch_by_company(user=user, name=name, company_id=company_id)
        if branch:
            serializer = BranchSerializer(branch, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            message = 'Это не ваш company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data={'detail': message}, status=status.HTTP_403_FORBIDDEN)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except ObjectDoesNotExist as e:
        message = f'Такой company не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def update_branch_view(request, pk):
    """Контроллер для обновления информации branch"""
    user = request.user
    data = request.data

    try:
        branch = get_branch_by_id_service(user, pk)
        if branch:
            serializer = BranchSerializer(branch, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(data={'detail': message}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
