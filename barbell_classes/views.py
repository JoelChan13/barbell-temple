from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'barbell_classes/home.html')


def timetable(request):
    return HttpResponse('barbell_classes/timetable.html')