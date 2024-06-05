from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class BarbellClass(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.TextField(default='')
    duration = models.TextField(default='')
    difficulty = models.TextField(default='')
    description = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('barbellclass-detail', kwargs={'pk': self.pk})