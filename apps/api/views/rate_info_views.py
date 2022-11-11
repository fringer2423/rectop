import logging
import sys

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import RateInfoSerializer

from ..services.rate_info_service import get_rate_info_service

logger = logging.getLogger('django')


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос выполнен успешно',
            schema=RateInfoSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        404: openapi.Response(
            description='Нет информации о тарифах'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о тарифах.',
    operation_summary='Получить rate info'
)
@api_view(['GET'])
def read_rate_info_view(request):
    """Контроллер для отдачи информации о rate_info"""

    try:
        rate_info = get_rate_info_service()
        serializer = RateInfoSerializer(rate_info, many=False)
        message = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    except ObjectDoesNotExist as e:
        message = f'Нет информации о тарифах {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_400_BAD_REQUEST
        )
