from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()  # Email field in registration form

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields in the registration form


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Email field in user update form

    class Meta:
        model = User
        fields = ['username', 'email']  # Fields in the user update form


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']  # Field in the user profile update form
