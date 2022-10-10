from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import serializers

from apps.core.models import User, Company


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериалайзер для авторизации
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели User
    """
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    """
    Сериалайзер модели User с Token
    """
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class CompanySerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField(read_only=True)
    owner = UserSerializer()

    class Meta:
        model = Company
        fields = '__all__'

    def get_created_at(self, obj):
        return obj.created_at.__format__('%Y-%m-%d %H:%M:%S')
