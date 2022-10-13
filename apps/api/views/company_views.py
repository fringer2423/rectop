from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import CompanySerializer

from ..services.company_services import get_company_by_id, create_company_by_company_name


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Название компании'
        )
    ],
    responses={
        201: openapi.Response(
            description='Компания создана',
            schema=CompanySerializer
        ),
        400: openapi.Response(
            description='Ошибка при создании'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        )
    },
    operation_description='Данный endpoint создает компанию, после возвращает информацию о ней. Поле owner показывает'
                          ' данные владельца компании.',
    operation_summary='Создать компанию'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_company(request):
    """
    Контроллер для создания компании
    :param request:
    :return: response
    """
    user = request.user

    try:
        company = create_company_by_company_name(user, request.data['name'])
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о компании по {id}. Поле owner показывает данные'
                          ' владельца компании.',
    operation_summary='Получить информацию о компании'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_company(request, pk):
    """Контроллер для отдачи информации о компании"""
    user = request.user

    try:
        company = get_company_by_id(user, pk)
        if company:
            serializer = CompanySerializer(company, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="put",
    manual_parameters=[
        openapi.Parameter(
            name='name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Название компании')
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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint изменяет информацию о компании по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в изменении. Поле owner показывает данные '
                          'владельца компании.',
    operation_summary='Изменить информацию о компании'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_company(request, pk):
    """Контроллер для обновления информации компании"""
    user = request.user
    data = request.data

    try:
        company = get_company_by_id(user, pk)
        if company:
            serializer = CompanySerializer(company, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)


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
            description='Компания не найдена'
        )
    },
    operation_description='Данный endpoint удаляет информацию о компании по {id}. Если владельцем компании является не'
                          ' авторизованный пользователь, будет отказано в изменении. Поле owner показывает данные '
                          'владельца компании.',
    operation_summary='Удалить информацию о компании'
)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_company(request, pk):
    """Контроллер для удаления информации компании"""
    user = request.user

    try:
        company = get_company_by_id(user, pk)
        if company:
            company.delete()
            return Response(data={'message': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Это не ваша компания'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as er:
        return Response(data={'message': 'Такой компании не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = 'Ошибка при обработке запроса ' + e.__str__()
        return Response(data={'message': message}, status=status.HTTP_400_BAD_REQUEST)
