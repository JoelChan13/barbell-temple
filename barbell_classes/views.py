from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class BarbellClassDetailView(DetailView):
    model = BarbellClass


class BarbellClassCreateView(LoginRequiredMixin, CreateView):
    model = BarbellClass
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BarbellClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BarbellClass
    fields = ['title', 'date', 'duration', 'difficulty', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        barbellclass = self.get_object()
        if self.request.user == barbellclass.author:
            return True
        return False


class BarbellClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BarbellClass
    success_url = "/"

    def test_func(self):
        barbellclass = self.get_object()
        if self.request.user == barbellclass.author:
            return True
        return False


def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})