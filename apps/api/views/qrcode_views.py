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

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.db import IntegrityError

from ..serializers import QRCodeSerializer, AllQRCodesSerializer

from ...core.models import User, QRCode

from ..services.qrcode_service import create_qrcode_by_branch_id_service, get_qrcode_by_id_service, \
    get_all_qrcode_service

logger: Logger = logging.getLogger('django')


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='type',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='branch_id'
        )
    ],
    responses={
        201: openapi.Response(
            description='QRCode создан',
            schema=QRCodeSerializer
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
        406: openapi.Response(
            description='QRCode уже создан для этого branch'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint создает QRCode по {id} branch, после возвращает информацию о QRCode.',
    operation_summary='Создать QRCode'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_qrcode_view(request: WSGIRequest) -> Response:
    """Контроллер для создания qrcode"""
    user: QuerySet[User] = request.user

    try:
        branch_id: int = request.data['branch_id']
        qr_code: QuerySet[QRCode] | None = create_qrcode_by_branch_id_service(
            user=user,
            branch_id=branch_id
        )
        if not (qr_code is None):
            serializer: Serializer[QRCodeSerializer] = QRCodeSerializer(
                qr_code,
                many=False,
                context={"request": request}
            )
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
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

    except IntegrityError as e:
        message: str = f'QRCode уже создан для этого branch {e}'
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
            schema=QRCodeSerializer
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
            description='QRCode не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о QRCode по {id}.',
    operation_summary='Получить QRCode'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_qrcode_view(request: WSGIRequest, pk: int) -> Response:
    """Контроллер для отдачи информации о QRCode"""
    user: QuerySet[User] = request.user

    try:
        qr_code: QuerySet[QRCode] | None = get_qrcode_by_id_service(user=user, qrcode_id=pk)
        if not (qr_code is None):
            serializer: Serializer[QRCodeSerializer] = QRCodeSerializer(
                qr_code,
                many=False,
                context={"request": request}
            )
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
        message: str = f'Такой QRCode не найден {e}'
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
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=AllQRCodesSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        404: openapi.Response(
            description='QRCode не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех QRCode.',
    operation_summary='Получить все QRCode'
)
@api_view(['GET'])
def read_all_qrcodes_view(request: WSGIRequest) -> Response:
    """Контроллер для отдачи информации о всех QRCode"""

    try:
        qr_code_list: QuerySet[QRCode] = get_all_qrcode_service()
        serializer: Serializer[AllQRCodesSerializer] = AllQRCodesSerializer(
            qr_code_list,
            many=True,
            context={"request": request}
        )
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist as e:
        message: str = 'QRCodes не найдены'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message: str = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )
