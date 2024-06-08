from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

class BarbellClass(models.Model):
    title = models.CharField(max_length=100, help_text="Enter the title of the barbell class (e.g., 'Beginner Strength Training')")
    image = CloudinaryField('image', default='placeholder')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    class_datetime = models.DateTimeField(default=timezone.now, help_text="Enter the date and time of the class (yyyy/mm/dd hours:minutes)")
    duration = models.TextField(default='', help_text="Enter the duration of the class (e.g., '1 hour')")
    difficulty = models.TextField(default='', help_text="Enter the difficulty level of the class (e.g., 'Beginner', 'Intermediate', 'Advanced')")
    description = models.TextField(help_text="Provide a detailed description of the class")
    available_spots = models.IntegerField(default=0, help_text="Number of available spots")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('barbellclass-detail', kwargs={'pk': self.pk})

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollment_set')
    barbell_class = models.ForeignKey(BarbellClass, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.barbell_class.title}"