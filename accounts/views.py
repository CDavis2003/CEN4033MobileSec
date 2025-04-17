from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, generics
# from .serializers import RegisterSerializer
from .models import * 
from core.utils import generate_rsa_keypair
from .forms import *



# Create your views here.
# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer

#     def perform_create(self, serializer):
#         user = serializer.save()
#         public, private = generate_rsa_keypair()
#         Credential.objects.create(user=user, public_key=public, private_key=private)

# class ListUsersView(APIView):
#     def get(self, request):
#         users = CustomUser.objects.all().values('id', 'username', 'email')
#         return Response(list(users))

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            public, private = generate_rsa_keypair()
            Credential.objects.create(user=user, public_key=public, private_key=private)
            return redirect('login-page')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return render(request, 'accounts/success.html', {'user': user})
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})