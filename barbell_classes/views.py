from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_barbellclasses(request):
    return HttpResponse("Hello, Barbell Fam!")