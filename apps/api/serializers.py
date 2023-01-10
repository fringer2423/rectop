from collections import OrderedDict
from datetime import datetime

from django.db.models import QuerySet
from rest_framework.fields import SerializerMethodField, UUIDField, CharField
from rest_framework.serializers import Serializer
from rest_framework.utils.serializer_helpers import ReturnDict
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import serializers

from apps.core.models import User, Company, Branch, Schedule, WorkDay, Telebot, Connect, Review, ReviewSettings, \
    Answer, QRCode, RateInfo, Rate


def format_data(field: datetime) -> str | None:
    """
    Функция форматирует дату в нужный формат
    :param field: поле Datetime field
    :return: datetime format
    """

    if field is None:
        return None
    else:
        return field.__format__('%Y-%m-%d %H:%M:%S')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Сериалайзер для авторизации"""

    def validate(self, attrs: OrderedDict) -> dict:
        data: dict = super().validate(attrs)

        serializer: dict = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели User"""
    is_admin: SerializerMethodField = SerializerMethodField(read_only=True)
    rate: SerializerMethodField = SerializerMethodField(read_only=True)
    is_verified: SerializerMethodField = SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[User] = User
        fields: list[str] = [
            'id', 'first_name', 'last_name', 'email', 'description', 'phone_number', 'rate', 'job_title', 'is_admin',
            'rate', 'is_verified'
        ]

    def get_is_admin(self, obj: QuerySet[User]) -> bool:
        return obj.is_staff

    def get_is_verified(self, obj: QuerySet[User]) -> bool:
        return obj.is_verified

    def get_rate(self, obj: QuerySet[User]) -> ReturnDict | None:
        # noinspection PyBroadException
        try:
            return RateSerializer(obj.rate, many=False).data
        except Exception as e:
            return None


class UserSerializerWithToken(UserSerializer):
    """Сериалайзер модели User с Token"""
    token: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[User] = User
        fields: list = ['id', 'username', 'email', 'is_admin', 'token', 'is_verified']

    def get_token(self, obj: QuerySet[User]) -> str:
        return str(RefreshToken.for_user(obj).access_token)


class CompanySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Company"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)
    owner: Serializer[UserSerializer] = UserSerializer()

    class Meta:
        model: QuerySet[Company] = Company
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[Company]) -> str | None:
        return format_data(obj.created_at)


class WorkDaySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели WorkDay"""

    class Meta:
        model: QuerySet[WorkDay] = WorkDay
        fields: str = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Schedule"""
    monday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    tuesday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    wednesday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    thursday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    friday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    saturday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    sunday: Serializer[WorkDaySerializer] = WorkDaySerializer()
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[Schedule] = Schedule
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[Schedule]) -> str | None:
        return format_data(obj.created_at)


class BranchSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Branch"""
    schedule: Serializer[ScheduleSerializer] = ScheduleSerializer()
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)
    last_date_load_reviews: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[Branch] = Branch
        fields: str = '__all__'
        read_only_fields: tuple = ('company', 'is_detected')

    def get_created_at(self, obj: QuerySet[Branch]) -> str | None:
        return format_data(obj.created_at)

    def get_last_date_load_reviews(self, obj: QuerySet[Branch]) -> str | None:
        return format_data(obj.last_date_load_reviews)


class TelebotSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Telebot"""

    class Meta:
        model: QuerySet[Telebot] = Telebot
        fields: str = '__all__'


class ConnectSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Connect"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[Connect] = Connect
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[Connect]) -> str | None:
        return format_data(obj.created_at)


class ReviewSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Review"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)
    answered_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)
    answer: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[Review] = Review
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[Review]) -> str | None:
        return format_data(obj.created_at)

    def get_answered_at(self, obj: QuerySet[Review]) -> str | None:
        return format_data(obj.answered_at)

    def get_answer(self, obj: QuerySet[Review]) -> ReturnDict | None:
        # noinspection PyBroadException
        try:
            return AnswerSerializer(obj.answer, many=False).data
        except Exception as e:
            return None


class ReviewSettingsSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Review settings"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[ReviewSettings] = ReviewSettings
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[ReviewSettings]) -> str | None:
        return format_data(obj.created_at)


class AnswerSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Answer"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model: QuerySet[Answer] = Answer
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[Answer]) -> str | None:
        return format_data(obj.created_at)


class QRCodeSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели QRCode"""
    created_at: SerializerMethodField = serializers.SerializerMethodField(read_only=True)
    branch: Serializer[BranchSerializer] = BranchSerializer()

    class Meta:
        model: QuerySet[QRCode] = QRCode
        fields: str = '__all__'

    def get_created_at(self, obj: QuerySet[QRCode]) -> str | None:
        return format_data(obj.created_at)


class AllQRCodesSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели QRCode. Отдает только 2 поля"""

    class Meta:
        model: QuerySet[QRCode] = QRCode
        fields: list = ['slug_name', 'branch']


class RateSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Rate"""

    class Meta:
        model: QuerySet[Rate] = Rate
        fields: str = '__all__'


class RateInfoSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Rate info"""

    class Meta:
        model: QuerySet[RateInfo] = RateInfo
        fields: str = '__all__'


class TaskSerializer(serializers.Serializer):
    """Сериалайзер для Task"""
    id: UUIDField = UUIDField()
    status: CharField = CharField()
    result: CharField = CharField()
