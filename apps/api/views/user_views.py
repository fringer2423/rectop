from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..serializers import MyTokenObtainPairSerializer, UserSerializerWithToken, UserSerializer

from ..services.user_services import create_user_by_data


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Контроллер для авторизации
    """
    serializer_class = MyTokenObtainPairSerializer

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
            )
        },
        operation_description='Данный endpoint позволяет авторизовать пользователя.',
        operation_summary='Авторизовать пользователя'
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


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
        )
    },
    operation_description='Данный endpoint позволяет зарегистрировать пользователя.',
    operation_summary='Зарегистрировать пользователя'
)
@api_view(['POST'])
def register_user(request):
    """
    Контроллер для регистрации новых пользователей
    :param request:
    :return: response: Данные пользователя с Token
    """
    data = request.data
    try:
        user = create_user_by_data(data)

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except Exception as e:
        message = {'detail': f'Пользователем с таким email уже существует {e}'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


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
        )
    },
    operation_description='Данный endpoint возвращает базовые данные о пользователе.',
    operation_summary='Получить информацию о пользователе'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_user_profile(request):
    """
    Контроллер для отдачи информации о текущем пользователе
    :param request:
    :return: response: информация о пользователе
    """
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


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
        )
    },
    operation_description='Данный endpoint изменяет базовые данные о пользователе.',
    operation_summary='Изменить информацию о пользователе'
)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    """
    Контроллер обновления пользовательских настроек
    :param request:
    :return: response
    """
    user = request.user
    data = request.data
    try:
        serializer = UserSerializer(user, many=False, partial=True, data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(data={'message': 'Ошибка при обработке запроса'}, status=status.HTTP_400_BAD_REQUEST)
