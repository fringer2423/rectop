from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from apps.core.models import Company

from ..serializers import CompanySerializer


@swagger_auto_schema(
    method="post",
    manual_parameters=[openapi.Parameter('name', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True)],
    responses={201: openapi.Response(description='Компания создана', schema=CompanySerializer),
               400: openapi.Response(description='Ошибка при создании'),
               401: openapi.Response(description='Пустой или неправильный токен')},
    operation_description='Данный endpoint создает компанию, после возвращает информацию о ней. Поле owner показывает'
                          ' данные владельца компании.',
    operation_summary='Создать компанию'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCompany(request):
    """
    Контроллер для создания компании
    :param request:
    :return: response
    """
    user = request.user

    try:

        company = Company.objects.create(
            owner=user,
            name=request.data['name']
        )

        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as er:
        message = f'Ошибка при создании {er}'
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={200: openapi.Response(description='Запрос выполнен успешно', schema=CompanySerializer),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Компания не найдена')},
    operation_description='Данный endpoint возвращает базовые данные о компании по {id}. Поле owner показывает данные'
                          ' владельца компании.',
    operation_summary='Получить информацию о компании'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCompany(request, pk):
    """Контроллер для отдачи информации о компании"""
    user = request.user

    try:
        company = Company.objects.get(pk=pk)

        if company.owner != user:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CompanySerializer(company, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method="post",
    manual_parameters=[openapi.Parameter('name', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True)],
    responses={200: openapi.Response(description='Запрос выполнен успешно', schema=CompanySerializer),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен'),
               403: openapi.Response(description='Ошибка доступа'),
               404: openapi.Response(description='Компания не найдена')},
    operation_description='Данный endpoint изменяет информацию о компании по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в изменении. Поле owner показывает данные '
                          'владельца компании.',
    operation_summary='Изменить информацию о компании'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateCompany(request, pk):
    user = request.user

    try:
        company = Company.objects.get(pk=pk)

        if company.owner != user:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

        company.name = request.data['name']
        company.save()

        serializer = CompanySerializer(company, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception:
        return Response(data={'message': 'Неверный запрос'}, status=status.HTTP_400_BAD_REQUEST)
