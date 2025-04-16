from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    high_score = models.IntegerField(default=0)

class Credential(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    pub_key = models.TextField()
    pass_hash = models.TextField()  # SHA-256 hash (with salt)
