from django.shortcuts import render
from .models import BarbellClass
from django.http import HttpResponse

barbellclass_updates = [
    {
        'author': 'Joel',
        'title': 'Barbell Class 1',
        'content': 'First class content',
        'date_posted': 'May 10, 2024'
    },
    {
        'author': 'Carl',
        'title': 'Barbell Class 2',
        'content': 'Second class content',
        'date_posted': 'May 11, 2024'
    }
]

def home(request):
    context = {
        'barbellclass_updates': BarbellClass.objects.all
    }
    return render(request, 'barbell_classes/home.html', context)


def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})