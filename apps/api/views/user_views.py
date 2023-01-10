import logging
import sys

from logging import Logger

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import QueryDict

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers import MyTokenObtainPairSerializer, UserSerializerWithToken, UserSerializer

from ..services.user_services import create_user_by_data_service, get_user_by_slug_service, verify_user_service, \
    generate_new_verify_code_for_user_service, verify_user_by_code_service

from ...tasks.tasks import send_email_task

from ...core.models import User

logger: Logger = logging.getLogger('django')


class MyTokenObtainPairView(TokenObtainPairView):
    """Контроллер для авторизации"""
    serializer_class: Serializer[MyTokenObtainPairSerializer] = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='email',
                in_=openapi.FORMAT_EMAIL,
                type=openapi.FORMAT_EMAIL,
                required=True,
                description='Email'
            ),
            openapi.Parameter(
                name='password',
                in_=openapi.TYPE_STRING,
                type=openapi.TYPE_STRING,
                required=True,
                description='Пароль'
            )
        ],
        responses={
            200: openapi.Response(
                description='Пользователь авторизован',
                schema=MyTokenObtainPairSerializer
            ),
            400: openapi.Response(
                description='Ошибка авторизации'
            ),
            401: openapi.Response(
                description='Пользователь с такими данными не найден'
            ),
            405: openapi.Response(
                description='Данный метод запроса запрещен'
            )
        },
        operation_description='Данный endpoint позволяет авторизовать пользователя.',
        operation_summary='Авторизовать пользователя'
    )
    def post(self, request: WSGIRequest, *args, **kwargs) -> Response:
        serializer: Serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - Invalid token / {e.args[0]}')
            raise InvalidToken(e.args[0])
        return Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='first_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Имя'
        ),
        openapi.Parameter(
            name='last_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Фамилия'
        ),
        openapi.Parameter(
            name='email',
            in_=openapi.FORMAT_EMAIL,
            type=openapi.FORMAT_EMAIL,
            required=True,
            description='EMail'
        ),
        openapi.Parameter(
            name='password',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=True,
            description='Пароль'
        )
    ],
    responses={
        201: openapi.Response(
            description='Пользователь зарегистрирован',
            schema=UserSerializerWithToken
        ),
        400: openapi.Response(
            description='Ошибка при регистрации'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint позволяет зарегистрировать пользователя.',
    operation_summary='Зарегистрировать user'
)
@api_view(['POST'])
def register_user_view(request: WSGIRequest) -> Response:
    """Контроллер для регистрации новых пользователей"""
    data: QueryDict = request.data
    try:
        user: QuerySet[User] = create_user_by_data_service(data)
        serializer: Serializer[UserSerializerWithToken] = UserSerializerWithToken(user, many=False)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        subject: str = 'Администратор Rectop'
        body: str = f'Для активации аккаунта перейдите по ссылке http://127.0.0.1:3000/auth/verify/{user.slug} \n ' \
                    f'Спасибо за регистрацию!'
        send_email_task.delay(subject, body, user.email.__str__())
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED
        )

    except KeyError as e:
        message: str = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    except Exception as e:
        message: str = f'Пользователем с таким email уже существует {e}'
        logger.critical(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
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
            description='Запрос прошел успешно',
            schema=UserSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о пользователе.',
    operation_summary='Получить user'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_user_profile_view(request: WSGIRequest) -> Response:
    """Контроллер для отдачи информации о текущем пользователе"""
    user: QuerySet[User] = request.user
    serializer: Serializer[UserSerializer] = UserSerializer(user, many=False)
    logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - Запрос выполнен успешно')
    return Response(
        data=serializer.data
    )


@swagger_auto_schema(
    method="put",
    manual_parameters=[
        openapi.Parameter(
            name='first_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Имя'
        ),
        openapi.Parameter(
            name='last_name',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Фамилия'
        ),
        openapi.Parameter(
            name='email',
            in_=openapi.FORMAT_EMAIL,
            type=openapi.FORMAT_EMAIL,
            required=False,
            description='EMail'
        ),
        openapi.Parameter(
            name='password',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Пароль'
        ),
        openapi.Parameter(
            name='description',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Описание'
        ),
        openapi.Parameter(
            name='phone_number',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Номер телефона'
        ),
        openapi.Parameter(
            name='job_title',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Должность'
        )
    ],
    responses={
        200: openapi.Response(
            description='Запрос прошел успешно',
            schema=UserSerializer
        ),
        400: openapi.Response(
            description='Ошибка при обработке запроса'
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
    operation_description='Данный endpoint изменяет базовые данные о пользователе.',
    operation_summary='Изменить user'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile_view(request: WSGIRequest) -> Response:
    """Контроллер обновления пользовательских настроек"""
    user: QuerySet[User] = request.user
    data: QueryDict = request.data
    try:
        serializer: Serializer[UserSerializer] = UserSerializer(user, many=False, partial=True, data=data)
        if serializer.is_valid():
            serializer.save()
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
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


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос прошел успешно',
            schema=UserSerializer
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        404: openapi.Response(
            description='Пользователь с таким slug не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint проводит верификацию user и активирует аккаунт.',
    operation_summary='Верифицировать user'
)
@api_view(['GET'])
def verify_user_view(request: WSGIRequest, slug: str) -> Response:
    """Контроллер для верификации пользователя"""
    try:
        user: QuerySet[User] = get_user_by_slug_service(slug)
        logger.error(f'!!!!!!!!!!!! {user}')
        user: QuerySet[User] = verify_user_service(user)
        serializer: Serializer[UserSerializerWithToken] = UserSerializerWithToken(user, many=False)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    except ObjectDoesNotExist as e:
        message: str = f'Такой slug не найден {e}'
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


@swagger_auto_schema(
    method="get",
    responses={
        200: openapi.Response(
            description='Запрос прошел успешно',
        ),
        400: openapi.Response(
            description='Ошибка при запросе'
        ),
        401: openapi.Response(
            description='Пустой или неправильный токен'
        ),
        404: openapi.Response(
            description='Пользователь не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        )
    },
    operation_description='Данный endpoint отправляет на email код подтверждения user.',
    operation_summary='Отправить код подтверждения user'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_verify_code_user_view(request: WSGIRequest) -> Response:
    """Контроллер для отправки кода верификации пользователя"""
    try:
        user: QuerySet[User] = request.user
        user = generate_new_verify_code_for_user_service(user.id)
        subject: str = 'Администратор Rectop'
        body: str = f'Приветствуем вас, {user.get_full_name()}! \n Ваш код подтверждения: {user.verify_code}'
        email: str = user.email.__str__()
        send_email_task.delay(subject, body, email)
        message: str = 'Запрос выполнен успешно'
        logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
        return Response(
            data={'detail': message},
            status=status.HTTP_200_OK
        )
    except ObjectDoesNotExist as e:
        message: str = f'Такой user не найден {e}'
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


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter(
            name='verify_code',
            in_=openapi.TYPE_STRING,
            type=openapi.TYPE_STRING,
            required=False,
            description='Проверочный код'
        ),
    ],
    responses={
        200: openapi.Response(
            description='Запрос прошел успешно',
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
            description='Пользователь не найден'
        ),
        405: openapi.Response(
            description='Данный метод запроса запрещен'
        ),
        422: openapi.Response(
            description='Отсутствует обязательное поле'
        )
    },
    operation_description='Данный endpoint проверяет код подтверждения user.',
    operation_summary='Проверить код подтверждения user'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_code_user_view(request: WSGIRequest) -> Response:
    """Контроллер для верификации пользователя по коду"""
    try:
        user: QuerySet[User] = request.user
        verify_code: str = request.data['verify_code']
        if verify_user_by_code_service(user, verify_code):
            message: str = 'Запрос выполнен успешно'
            logger.info(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={'detail': message},
                status=status.HTTP_200_OK
            )
        else:
            message: str = 'Этот код не подходит'
            logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message} / user id:{user.id}')
            return Response(
                data={
                    'detail': message
                },
                status=status.HTTP_403_FORBIDDEN
            )
    except ObjectDoesNotExist as e:
        message: str = f'Такой user не найден {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_404_NOT_FOUND
        )

    except KeyError as e:
        message: str = f'Ошибка при обработке запроса. Отсутствует поле {e}'
        logger.warning(f'{__name__}.{sys._getframe().f_code.co_name} - {message}')
        return Response(
            data={
                'detail': message
            },
            status=status.HTTP_422_UNPROCESSABLE_ENTITY
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
