from django.urls import path
from .views import BarbellClassListView
from . import views

urlpatterns = [
    path('', BarbellClassListView.as_view(), name='barbell_classes-home'),
    path('timetable/', views.timetable, name='barbell_classes-timetable'),
]