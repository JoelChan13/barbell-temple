from django.shortcuts import render
from django.views.generic import ListView
from .models import BarbellClass
from django.http import HttpResponse


def home(request):
    context = {
        'barbellclass_updates': BarbellClass.objects.all
    }
    return render(request, 'barbell_classes/home.html', context)

class BarbellClassListView(ListView):
    model = BarbellClass
    template_name = 'barbell_classes/home.html'
    context_object_name = 'barbellclass_updates'
    ordering = ['-date_posted']

def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})