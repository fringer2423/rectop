from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import serializers

from apps.core.models import User, Company, Branch, Schedule, WorkDay, Telebot, Connect, Review, ReviewSettings, \
    Answer, QRCode, RateInfo, Rate


def format_data(field):
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

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели User"""
    is_admin = serializers.SerializerMethodField(read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)
    is_verified = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'description', 'phone_number', 'rate', 'job_title',
                  'is_admin', 'rate', 'is_verified']

    def get_is_admin(self, obj):
        return obj.is_staff

    def get_is_verified(self, obj):
        return obj.is_verified

    def get_rate(self, obj):
        try:
            return RateSerializer(obj.rate, many=False).data
        except Exception as e:
            print(e)
            return None


class UserSerializerWithToken(UserSerializer):
    """Сериалайзер модели User с Token"""
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'token', 'is_verified']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class CompanySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Company"""
    created_at = serializers.SerializerMethodField(read_only=True)
    owner = UserSerializer()

    class Meta:
        model = Company
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class WorkDaySerializer(serializers.ModelSerializer):
    """Сериалайзер для модели WorkDay"""

    class Meta:
        model = WorkDay
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Schedule"""
    monday = WorkDaySerializer()
    tuesday = WorkDaySerializer()
    wednesday = WorkDaySerializer()
    thursday = WorkDaySerializer()
    friday = WorkDaySerializer()
    saturday = WorkDaySerializer()
    sunday = WorkDaySerializer()
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class BranchSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Branch"""
    schedule = ScheduleSerializer()
    created_at = serializers.SerializerMethodField(read_only=True)
    last_date_load_reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'
        read_only_fields = ('company', 'is_detected')

    def get_created_at(self, obj):
        return format_data(obj.created_at)

    def get_last_date_load_reviews(self, obj):
        return format_data(obj.last_date_load_reviews)


class TelebotSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Telebot"""

    class Meta:
        model = Telebot
        fields = '__all__'


class ConnectSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Connect"""
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Connect
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class ReviewSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Review"""
    created_at = serializers.SerializerMethodField(read_only=True)
    answered_at = serializers.SerializerMethodField(read_only=True)
    answer = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)

    def get_answered_at(self, obj):
        return format_data(obj.answered_at)

    def get_answer(self, obj):
        try:
            return AnswerSerializer(obj.answer, many=False).data
        except Exception as e:
            print(e)
            return None


class ReviewSettingsSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Review settings"""
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ReviewSettings
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class AnswerSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Answer"""
    created_at = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class QRCodeSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели QRCode"""
    created_at = serializers.SerializerMethodField(read_only=True)
    branch = BranchSerializer()

    class Meta:
        model = QRCode
        fields = '__all__'

    def get_created_at(self, obj):
        return format_data(obj.created_at)


class AllQRCodesSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели QRCode. Отдает только 2 поля"""

    class Meta:
        model = QRCode
        fields = ['slug_name', 'branch']


class RateSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Rate"""

    class Meta:
        model = Rate
        fields = '__all__'


class RateInfoSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Rate info"""

    class Meta:
        model = RateInfo
        fields = '__all__'


class TaskSerializer(serializers.Serializer):
    """Сериалайзер для Task"""
    id = serializers.UUIDField()
    status = serializers.CharField()
    result = serializers.CharField()
