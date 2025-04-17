from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('leaderboard/', views.leaderboard_page, name='leaderboard-page'),
]
