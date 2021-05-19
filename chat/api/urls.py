from django.urls import path
from .views import ChatListAPIView, MessageListAPIView, ChatDetailAPIView

app_name = "chat"

urlpatterns = [
    path('', ChatListAPIView.as_view()),
    path('messages/', MessageListAPIView.as_view()),
    path('<str:chat_id>/', ChatDetailAPIView.as_view()),
]
