from rest_framework import permissions, generics, mixins
from chat.models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        chat_id = self.request.query_params.get('chat_id')
        serializer.save(author=self.request.user, chat_id=chat_id)


class ChatListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Chat.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user_id = self.request.query_params.get('user_id')
        user_obj = get_object_or_404(User, user_chat_id=user_id)
        serializer.save(sender=self.request.user, receiver=user_obj)


class ChatDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Chat.objects.all()
    lookup_field = 'chat_id'
