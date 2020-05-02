from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from .serializers import UserRegisterSerializer
from accounts.api.permissions import AnonPermissionOnly

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# class RegisterView(APIView):
#   permission_classes = [permissions.AllowAny]
#   def post(self, request, *args, **kwargs):
#     if request.user.is_authenticated():
#       return Response({'detail': 'You are already registered and are authenticated.'}, status=400)
#     data = request.data
#     username = data.get('username')
#     email = data.get('username')
#     password = data.get('password')
#     password2 = data.get('password2')

#     qs = User.objects.filter(
#       Q(username__iexact=username),
#       Q(email__iexact=username)
#     )
#     if password!=password2:
#       return Response({'password': 'Password must match.'}, status=401)
#     if qs.exists():
#       return Response({'detail': 'This user already exists'}, status=401)
#     else:
#       user = User.objects.create(username=username, email=email)
#       user.set_password(password)
#       user.save()
#       return Response({'detail':'Thank you for registering.'}, status=201)
#     return Response({'detail': 'Invalid Request'}, status=400)




class RegisterAPIView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserRegisterSerializer
  permission_classes = [AnonPermissionOnly]

  def get_serializer_context(self, *args, **kwargs):
    return {'request': self.request}






class AuthAPIView(APIView):
  permission_classes = [AnonPermissionOnly]

  def post(self, request, *args, **kwargs):
    if request.user.is_authenticated():
      return Response({'detail': 'You are already authenticated'}, status=400)
    data = request.data
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    get_tokens_for_user(user)
    return Response({'token': token})

