from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserProfileV1Serializer, UserProfileV2Serializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProfileV1View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileV1Serializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ProfileV2View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileV2Serializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
