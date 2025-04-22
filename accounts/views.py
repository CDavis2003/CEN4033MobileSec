from time import sleep

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from django.http import HttpResponseForbidden
from .models import * 
from core.utils import generate_rsa_keypair
from .forms import *


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            public, private = generate_rsa_keypair()
            Credential.objects.create(user=user, public_key=public, private_key=private)
            return redirect('accounts:login-page')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                print("✅ Login successful!")
                login(request, user)
                return redirect('home-page')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutUser(request):
    user = request.user
    logout(request)
    if user.is_authenticated and user.is_guest:
        user.delete()
    render(request, 'logout.html')
    sleep(3)
    return redirect('accounts:login-page')

def guest_login(request):
    username = f"guest_{get_random_string(10)}"
    email = f"{username}@guest.local"

    user = CustomUser.objects.create_user(username=username, email=email)
    user.is_guest = True
    user.set_unusable_password()
    user.save()

    public_key, private_key = generate_rsa_keypair()
    Credential.objects.create(user=user, public_key=public_key, private_key=private_key)

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    print("👤 Guest login successful!")
    return redirect('home-page')