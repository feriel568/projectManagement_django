from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')

    def __str__(self):
        return f"{self.user.username} - Profil"
