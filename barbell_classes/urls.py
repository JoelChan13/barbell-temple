from django.urls import path
from .views import BarbellClassListView, BarbellClassDetailView
from . import views

urlpatterns = [
    path('', BarbellClassListView.as_view(), name='barbell_classes-home'),
    path('barbellclass/<int:pk>', BarbellClassDetailView.as_view(), name='barbellclass-detail'),
    path('timetable/', views.timetable, name='barbell_classes-timetable'),
]