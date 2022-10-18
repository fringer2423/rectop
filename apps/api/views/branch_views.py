from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import BranchSerializer

from ..services.company_services import get_company_by_id
from ..services.branch_service import get_branch_by_id


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех филиалах по {id} компании.',
    operation_summary='Получить информацию о филиалах'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_branch_list(request, pk):
    """Контроллер для отдачи информации о филиалах"""
    user = request.user

    try:
        company = get_company_by_id(user, pk)
        if company:
            serializer = BranchSerializer(company.branchs, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о всех филиалах по {id} компании.',
    operation_summary='Получить информацию о филиале'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_branch(request, pk):
    """Контроллер для отдачи информации о филиале"""
    user = request.user

    try:
        branch = get_branch_by_id(user=user, branch_id=pk)
        if branch:
            serializer = BranchSerializer(branch, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваш Филиал'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'detail': 'Такой филиал не найден'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
