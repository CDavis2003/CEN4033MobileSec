from django.db import models
from accounts.models import CustomUser
from questions.models import Question


class Game(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.score} pts on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.score > self.user.high_score:
            self.user.high_score = self.score
            self.user.save()

class Leaderboard(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    high_score = models.IntegerField(default=0)


