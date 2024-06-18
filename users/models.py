from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User model
    image = CloudinaryField('image', default='default.jpg', folder='profile_pictures')  # CloudinaryField for profile picture

    def __str__(self):
        return f'{self.user.username} Profile'