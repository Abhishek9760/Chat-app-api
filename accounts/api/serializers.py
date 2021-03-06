import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework_jwt.settings import api_settings

expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA

User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class UserPublicSerializer(serializers.ModelSerializer):
    # uri = serializers.SerializerMethodField(read_only=True)
    # friends = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'online',
            'user_chat_id',
            'timestamp',
            # 'uri'
        ]

    # def get_uri(self, obj):
    #     request = self.context.get('request')
    #     return api_reverse("api-status:detail", kwargs={"id": obj.id}, request=request)


class NestedUserPublicSerializer(serializers.ModelSerializer):
    friends = UserPublicSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'online',
                  'user_chat_id', 'email', 'timestamp', 'friends']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'expires',
            'token',
            'message',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_message(self, obj):
        return "Thank you for registering. Please verify your email."

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                'User with this username already exists.')
        return value

    def get_token(self, obj):
        user = obj
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                'User with this email already exists.')
        return value

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        user_obj = User(username=validated_data.get('username'),
                        email=validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj
