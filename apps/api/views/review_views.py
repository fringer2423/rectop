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

from ..serializers import ReviewSerializer

from ..services.branch_service import get_branch_by_id_service
from ..services.review_service import create_review_by_branch_id_service, get_review_by_id_service, \
    get_all_review_by_company_id_service

logger = logging.getLogger('django')


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
        openapi.Parameter(
            name='connect_id',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Id connect'
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
    operation_description='Данный endpoint создает review по {id} branch и connect_id, после возвращает информацию'
                          ' о review.',
    operation_summary='Создать review'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review_view(request):
    """Контроллер для создания review"""
    user = request.user

    try:
        try:
            connect_id = request.data['connect_id']
        except Exception as e:
            print(e)
            connect_id = None
        review = create_review_by_branch_id_service(
            user=user,
            branch_id=request.data['branch_id'],
            full_name=request.data['full_name'],
            link=request.data['link'],
            rating=request.data['rating'],
            connect_id=connect_id
        )
        if review:
            serializer = ReviewSerializer(review, many=False)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найден {e}'
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
def read_review_view(request, pk):
    """Контроллер для отдачи информации о review"""
    user = request.user

    try:
        review = get_review_by_id_service(user=user, review_id=pk)
        if review:
            serializer = ReviewSerializer(review, many=False)
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой review не найден {e}'
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
def read_review_list_view(request, pk):
    """Контроллер для отдачи информации о всех review branch"""
    user = request.user

    try:
        branch = get_branch_by_id_service(user=user, branch_id=pk)
        if branch:

            query = request.query_params.get('keyword')
            if query is None:
                query = ''
            review_list = branch.review_set.all()
            page = request.query_params.get('page')
            paginator = Paginator(review_list, 10)

            try:
                review_list = paginator.page(page)
            except PageNotAnInteger:
                review_list = paginator.page(1)
            except EmptyPage:
                review_list = paginator.page(paginator.num_pages)

            if page is None:
                page = 1

            page = int(page)

            serializer = ReviewSerializer(review_list, many=True)
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
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой branch не найден {e}'
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
def update_review_view(request, pk):
    """Контроллер для обновления информации review"""
    user = request.user
    data = request.data

    try:
        review = get_review_by_id_service(user=user, review_id=pk)
        if review:
            serializer = ReviewSerializer(review, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваш branch'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой review не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
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
def delete_review_view(request, pk):
    """Контроллер для удаления информации review"""
    user = request.user

    try:
        review = get_review_by_id_service(user=user, review_id=pk)
        if review:
            review.delete()
            message = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_200_OK
            )
        else:
            message = 'Это не ваша company'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой review не найден {e}'
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
    operation_description='Данный endpoint возвращает базовые данные о всех review по {id} company.',
    operation_summary='Получить reviews list'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_review_list_all_view(request, pk):
    """Контроллер для отдачи информации о всех review компании"""
    user = request.user

    try:
        review_list = get_all_review_by_company_id_service(user=user, company_id=pk)
        if review_list:

            query = request.query_params.get('keyword')
            if query is None:
                query = ''
            page = request.query_params.get('page')
            paginator = Paginator(review_list, 10)

            try:
                review_list = paginator.page(page)
            except PageNotAnInteger:
                review_list = paginator.page(1)
            except EmptyPage:
                review_list = paginator.page(paginator.num_pages)

            if page is None:
                page = 1

            page = int(page)

            serializer = ReviewSerializer(review_list, many=True)
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
            message = 'Это не ваш review'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )

    except ObjectDoesNotExist as e:
        message = f'Такой review не найден {e}'
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
