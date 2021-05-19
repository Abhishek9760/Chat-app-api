from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import permissions, generics, pagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.serializers import NestedUserPublicSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = NestedUserPublicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.filter(active=True)
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}


class ToggleFriendAPIView(APIView):
    def get(self, request, username, format=None):
        user = request.user
        res_text = ""
        user_obj = get_object_or_404(User, username=username)
        if user.is_authenticated:
            if user.friends.filter(username=username).exists():
                user.friends.remove(user_obj)
                res_text = f"removed"
            else:
                user.friends.add(user_obj)
                res_text = f"added"
        return Response({"message": res_text}, status=200)

# class UserStatusAPIView(generics.ListAPIView):
#     serializer_class = StatusInlineUserSerializer
#     # pagination_class = StatusAPIPagination

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get('username')
#         if not username:
#             return Status.objects.none()
#         return Status.objects.filter(user__username=username)


# class UserStatusAPIView(StatusAPIView):
#     serializer_class = StatusInlineUserSerializer
#     # pagination_class = StatusAPIPagination

#     def get_queryset(self, *args, **kwargs):
#         username = self.kwargs.get('username')
#         if not username:
#             return Status.objects.none()
#         return Status.objects.filter(user__username=username)

#     def post(self, request, *args, **kwargs):
#         return Response({"detail": "Not Allowed Here"}, status=400)
