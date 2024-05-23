from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for Templar {username}!')
            return redirect('barbell_classes-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})