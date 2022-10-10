from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..serializers import MyTokenObtainPairSerializer, UserSerializerWithToken, UserSerializer

from apps.core.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Контроллер для авторизации
    """
    serializer_class = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('email', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('password', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True)
        ],
        responses={200: openapi.Response(description='Пользователь авторизован', schema=MyTokenObtainPairSerializer),
                   400: openapi.Response(description='Ошибка авторизации')},
        operation_description='Данный endpoint позволяет авторизовать пользователя.',
        operation_summary='Авторизовать пользователя'
    )
    def post(self, request, *args, **kwargs):
        super().post(self, request, *args, **kwargs)


@swagger_auto_schema(
    method="post",
    manual_parameters=[
        openapi.Parameter('first_name', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('username', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('email', openapi.FORMAT_EMAIL, type=openapi.TYPE_STRING, required=True),
        openapi.Parameter('password', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=True)
    ],
    responses={201: openapi.Response(description='Пользователь зарегистрирован', schema=UserSerializerWithToken),
               400: openapi.Response(description='Ошибка при регистрации')},
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
        user = User.objects.create(
            first_name=data['first_name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Пользователем с таким email уже существует'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="get",
    responses={200: openapi.Response(description='Запрос прошел успешно', schema=UserSerializer),
               400: openapi.Response(description='Ошибка при запросе'),
               401: openapi.Response(description='Пустой или неправильный токен')},
    operation_description='Данный endpoint возвращает базовые данные о пользователе.',
    operation_summary='Получить информацию о пользователе'
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    """
    Контроллер для отдачи информации о текущем пользователе
    :param request:
    :return: response: информация о пользователе
    """
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    manual_parameters=[openapi.Parameter('first_name', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=False),
                       openapi.Parameter('last_name', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=False),
                       openapi.Parameter('email', openapi.FORMAT_EMAIL, type=openapi.TYPE_STRING, required=False),
                       openapi.Parameter('password', openapi.TYPE_STRING, type=openapi.TYPE_STRING, required=False),
                       openapi.Parameter('description', openapi.FORMAT_EMAIL, type=openapi.TYPE_STRING, required=False),
                       openapi.Parameter('phone_number', openapi.FORMAT_EMAIL, type=openapi.TYPE_STRING,
                                         required=False),
                       openapi.Parameter('job_title', openapi.FORMAT_EMAIL, type=openapi.TYPE_STRING, required=False)],
    responses={200: openapi.Response(description='Запрос прошел успешно', schema=UserSerializer),
               401: openapi.Response(description='Пустой или неправильный токен')},
    operation_description='Данный endpoint изменяет базовые данные о пользователе.',
    operation_summary='Изменить информацию о пользователе'
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    """
    Контроллер обновления пользовательских настроек
    :param request:
    :return: response
    """
    user = request.user
    data = request.data

    serializer = UserSerializer(user, many=False, partial=True, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
