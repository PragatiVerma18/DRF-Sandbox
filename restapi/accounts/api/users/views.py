from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, pagination
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserPublicSerializer
from status.api.serializers import StatusInlineUserSerializer
from status.models import Status



class UserDetailAPIView(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = User.objects.filter(is_active = True)
  serializer_class = UserPublicSerializer
  lookup_field = 'username'

  def get_serializer_context(self):
    return {'request': self.request}

# class CustomPagination(pagination.PageNumberPagination):
#   page_size = 5


class UserStatusAPIView(generics.ListAPIView):
  serializer_class = StatusInlineUserSerializer
  # pagination_class = pagination.PageNumberPagination

  def get_queryset(self, *args, **kwargs):
    username = self.kwargs.get("username",None)
    if username is None:
      return Status.objects.none()
    return Status.objects.filter(user__username=username)