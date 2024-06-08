from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relationship with User model
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')  # Image field for profile picture

    def __str__(self):
        return f'{self.user.username} Profile'  # String representation of the profile

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the save method of the parent class

        img = Image.open(self.image.path)  # Open the image using PIL

        if img.height > 300 or img.width > 300:  # Check if image is larger than 300x300
            output_size = (300, 300)  # Define the output size
            img.thumbnail(output_size)  # Resize the image to fit within the specified size
            img.save(self.image.path)  # Save the resized image
