from django.urls import path, include
from . import views

app_name = 'game'

urlpatterns = [
    path('play/', views.play_game, name='play-page'),
]