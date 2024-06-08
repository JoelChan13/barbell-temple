from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdateForm


def registration(request):
    if request.method == 'POST':  # Check if the request method is POST
        form = UserRegistrationForm(request.POST)  # Get the registration form data
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the form data
            username = form.cleaned_data.get('username')  # Get the username from the form data
            messages.success(request, f'Congratulations {username}, Welcome to The Barbell Temple !')  # Display success message
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()  # Create a new registration form instance
    return render(request, 'users/registration.html', {'form': form})  # Render the registration form


@login_required  # Require login to access profile view
def profile(request):
    if request.method == 'POST':  # Check if the request method is POST
        u_form = UserUpdateForm(request.POST, instance=request.user)  # Get the user update form data
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # Get the profile update form data
        if u_form.is_valid() and p_form.is_valid():  # Check if both forms are valid
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Has Been Updated')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)  # Create a new user update form instance
        p_form = UserProfileUpdateForm(instance=request.user.profile)  # Create a new profile update form instance

    context = {  # Create context dictionary with forms
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
