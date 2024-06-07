# urls.py
from django.urls import path
from .views import (
    BarbellClassListView,
    BarbellClassDetailView,
    BarbellClassCreateView,
    BarbellClassUpdateView,
    BarbellClassDeleteView,
    BarbellClassEnrol,
    BarbellClassUnenrol
)
from . import views

urlpatterns = [
    path('', BarbellClassListView.as_view(), name='barbell_classes-home'),
    path('barbellclass/<int:pk>', BarbellClassDetailView.as_view(), name='barbellclass-detail'),
    path('barbellclass/new/', BarbellClassCreateView.as_view(), name='barbellclass-create'),
    path('barbellclass/<int:pk>/update/', BarbellClassUpdateView.as_view(), name='barbellclass-update'),
    path('barbellclass/<int:pk>/delete/', BarbellClassDeleteView.as_view(), name='barbellclass-delete'),
    path('timetable/', views.timetable, name='barbell_classes-timetable'),
    path('mybarbellclasses/', views.my_barbellclasses, name='my_barbellclasses'),
    path('barbellclass/<int:pk>/enrol/', BarbellClassEnrol.as_view(), name='barbellclass-enrol'),
    path('barbellclass/<int:pk>/unenrol/', BarbellClassUnenrol.as_view(), name='barbellclass-unenrol'),
]
