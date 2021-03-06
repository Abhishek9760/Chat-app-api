from django.urls import path

from .views import UserDetailAPIView, ToggleFriendAPIView


app_name = "users"

urlpatterns = [
    path('<str:username>/', UserDetailAPIView.as_view(), name='detail'),
    path('<str:username>/toggle/', ToggleFriendAPIView.as_view())
    # path('<str:username>/status/', UserStatusAPIView.as_view(), name='status-list'),
]
