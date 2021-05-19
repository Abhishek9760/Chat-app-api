from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.api.urls')),
    path('api/chat/', include('chat.api.urls', namespace="chat")),
    # path('api/auth/', include('rest_framework.urls')),
    # path('api/status/', include('status.api.urls', namespace='api-status')),
    path('api/user/', include('accounts.api.user.urls', namespace='api-user')),
]
