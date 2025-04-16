from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    high_score = models.IntegerField(default=0)
    email = models.EmailField(unique=True)


class Credential(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    public_key = models.TextField()
    private_key = models.TextField()  # SHA-256 hash (with salt)
