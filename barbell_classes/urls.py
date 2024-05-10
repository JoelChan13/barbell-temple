from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_barbellclasses, name='barbell_classes-home'),
    path('about/', views.about, name='barbell_classes-about'),
]