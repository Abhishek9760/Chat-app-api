from rest_framework import serializers

from chat.models import Chat, Message
from accounts.api.serializers import UserPublicSerializer, NestedUserPublicSerializer


class MessageSerializer(serializers.ModelSerializer):
    author = UserPublicSerializer(read_only=True)

    class Meta:
        model = Message
        fields = [
            'id',
            'author',
            'content',
            'timestamp'
        ]

    def create(self, validated_data):
        chat_id = validated_data.get('chat_id')
        print(chat_id)
        chat_obj = Chat.objects.get(chat_id=chat_id)
        content, author = validated_data.get(
            'content'), validated_data.get('author')
        message_obj = Message(content=content, author=author)
        message_obj.save()
        message_obj.chat_set.add(chat_obj)
        message_obj.save()
        return message_obj


class ChatSerializer(serializers.ModelSerializer):
    sender = UserPublicSerializer(read_only=True)
    receiver = UserPublicSerializer(read_only=True)

    class Meta:
        model = Chat
        fields = [
            'id',
            'chat_id',
            'sender',
            'receiver',
        ]
