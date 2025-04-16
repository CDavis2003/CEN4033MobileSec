from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import RegisterSerializer
from .models import * 
from core.utils import generate_rsa_keypair


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        public, private = generate_rsa_keypair()
        Credential.objects.create(user=user, public_key=public, private_key=private)

class ListUsersView(APIView):
    def get(self, request):
        users = CustomUser.objects.all().values('id', 'username', 'email')
        return Response(list(users))
