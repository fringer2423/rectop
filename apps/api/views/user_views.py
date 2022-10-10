from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from ..serializers import MyTokenObtainPairSerializer, UserSerializerWithToken, UserSerializer

from apps.core.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    """
    Контроллер для авторизации
    """
    serializer_class = MyTokenObtainPairSerializer


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
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Пользователем с таким email уже существует'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    """
    Функция обновления пользовательских настроек
    :param request:
    :return: response
    """
    user = request.user
    data = request.data

    serializer = UserSerializer(user, many=False, partial=True, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)
