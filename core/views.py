from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_page(request):
    return render(request, 'core/home.html')

@login_required(login_url='login-page')
def leaderboard_page(request):
    return render(request, "core/leaderboard.html")