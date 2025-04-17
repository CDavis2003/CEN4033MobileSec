from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.question_text} (Answer: {'True' if self.correct_answer else 'False'})"
