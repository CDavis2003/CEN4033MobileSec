from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
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