from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='barbell_classes-home'),
    path('timetable/', views.timetable, name='barbell_classes-timetable'),
]