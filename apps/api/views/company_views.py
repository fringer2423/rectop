from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.core.exceptions import ObjectDoesNotExist

from ..serializers import CompanySerializer

from ..services.company_services import get_company_by_id_service, create_company_by_company_name_service


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
def create_company_view(request):
    """Контроллер для создания company"""
    user = request.user

    try:
        company = create_company_by_company_name_service(user, request.data['name'])
        serializer = CompanySerializer(company, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def read_company_view(request, pk):
    """Контроллер для отдачи информации о company"""
    user = request.user

    try:
        company = get_company_by_id_service(user, pk)
        if company:
            serializer = CompanySerializer(company, many=False)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша company'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой company не найдено {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def update_company_view(request, pk):
    """Контроллер для обновления информации company"""
    user = request.user
    data = request.data

    try:
        company = get_company_by_id_service(user, pk)
        if company:
            serializer = CompanySerializer(company, many=False, partial=True, data=data)
            if serializer.is_valid():
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша company'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist:
        return Response(data={'detail': 'Такой company не найдено'}, status=status.HTTP_404_NOT_FOUND)

    except KeyError as e:
        message = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        return Response(data={'detail': message}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)


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
def delete_company_view(request, pk):
    """Контроллер для удаления информации company"""
    user = request.user

    try:
        company = get_company_by_id_service(user, pk)
        if company:
            company.delete()
            return Response(data={'detail': 'Удаление прошло успешно'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'detail': 'Это не ваша company'}, status=status.HTTP_403_FORBIDDEN)

    except ObjectDoesNotExist as e:
        return Response(data={'detail': f'Такой company не найдено {e}'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        message = f'Ошибка при обработке запроса {e}'
        return Response(data={'detail': message}, status=status.HTTP_400_BAD_REQUEST)
