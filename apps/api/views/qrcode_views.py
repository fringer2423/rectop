from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from ..serializers import QRCodeSerializer, AllQRCodesSerializer

from ..services.qrcode_service import create_qrcode_by_branch_id_service, get_qrcode_by_id_service,\
    get_all_qrcode_service


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
def create_qrcode_view(request):
    """Контроллер для создания qrcode"""
    user = request.user

    try:
        branch_id = request.data['branch_id']
        qr_code = create_qrcode_by_branch_id_service(
            user=user,
            branch_id=branch_id
        )
        if qr_code:
            serializer = QRCodeSerializer(qr_code, many=False, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой branch не найден {e}'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except IntegrityError as e:
        return Response(
            data={'detail': f'QRCode уже создан для этого branch {e}'},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def read_qrcode_view(request, pk):
    """Контроллер для отдачи информации о QRCode"""
    user = request.user

    try:
        qr_code = get_qrcode_by_id_service(user=user, qrcode_id=pk)
        if qr_code:
            serializer = QRCodeSerializer(qr_code, many=False, context={"request": request})
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш branch'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой QRCode не найден {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def read_all_qrcodes_view(request):
    """Контроллер для отдачи информации о всех QRCode"""

    try:
        qr_code_list = get_all_qrcode_service()
        serializer = AllQRCodesSerializer(qr_code_list, many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой QRCode не найден {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
