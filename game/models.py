from django.db import models
from accounts.models import CustomUser

class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    high_score = models.IntegerField(default=0)
