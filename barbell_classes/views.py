from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import BarbellClass
from django.http import JsonResponse
from django.http import HttpResponse


def home(request):
    context = {
        'barbellclass_updates': BarbellClass.objects.all()
    }
    return render(request, 'barbell_classes/home.html', context)


class BarbellClassListView(ListView):
    model = BarbellClass
    template_name = 'barbell_classes/home.html'
    context_object_name = 'barbellclass_updates'
    ordering = ['-date_posted']


class BarbellClassDetailView(DetailView):
    model = BarbellClass


class BarbellClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BarbellClass
    fields = ['title', 'date', 'duration', 'difficulty', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('barbell_classes-home')


class BarbellClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BarbellClass
    fields = ['title', 'date', 'duration', 'difficulty', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    def handle_no_permission(self):
        return redirect('barbell_classes-home')


class BarbellClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BarbellClass
    success_url = "/"

    def test_func(self):
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    def handle_no_permission(self):
        return redirect('barbell_classes-home')


def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})


def my_barbellclasses(request):
    context = {
        'my_barbellclasses': BarbellClass.objects.filter(author=request.user)
    }
    return render(request, 'barbell_classes/my_barbellclasses.html', context)
