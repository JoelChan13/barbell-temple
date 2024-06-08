from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)  # Signal receiver for post_save signal and User model
def create_profile(sender, instance, created, **kwargs):
    if created:  # Check if a new user is created
        Profile.objects.create(user=instance)  # Create a profile for the new user


@receiver(post_save, sender=User)  # Signal receiver for post_save signal and User model
def save_profile(sender, instance, **kwargs):
    instance.profile.save()  # Save the profile whenever the User instance is saved
