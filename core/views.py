from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from game.models import *


# Create your views here.
User = get_user_model()

def home_page(request):
    return render(request, 'core/home.html')

@login_required(login_url='login-page')
def leaderboard_page(request):
    top_users = User.objects.order_by('-high_score')[:10]
    return render(request, 'core/leaderboard.html', {'top_users': top_users})


def settings_page(request):
    return render(request, "core/settings.html")