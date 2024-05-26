from django.urls import path
from .views import (
    BarbellClassListView,
    BarbellClassDetailView,
    BarbellClassCreateView
)
from . import views

urlpatterns = [
    path('', BarbellClassListView.as_view(), name='barbell_classes-home'),
    path('barbellclass/<int:pk>', BarbellClassDetailView.as_view(), name='barbellclass-detail'),
    path('barbellclass/new/', BarbellClassCreateView.as_view(), name='barbellclass-create'),
    path('barbellclass/<int:pk>/update/', BarbellClassUpdateView.as_view(), name='barbellclass-update'),
    path('timetable/', views.timetable, name='barbell_classes-timetable'),
]