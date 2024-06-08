# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from .models import BarbellClass, Enrollment
from django.http import JsonResponse, HttpResponse
from django.urls import reverse


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_enrolled'] = Enrollment.objects.filter(
                user=self.request.user,
                barbell_class=self.object
            ).exists()
        else:
            context['is_enrolled'] = False
        return context

class BarbellClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('barbell_classes-home')


class BarbellClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

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


class BarbellClassEnrol(LoginRequiredMixin, View):
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        if barbellclass.available_spots > 0:
            Enrollment.objects.get_or_create(user=request.user, barbell_class=barbellclass)
            barbellclass.available_spots -= 1
            barbellclass.save()
        return redirect('my_barbellclasses')


class BarbellClassUnenrol(LoginRequiredMixin, View):
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        enrollment = Enrollment.objects.filter(user=request.user, barbell_class=barbellclass)
        if enrollment.exists():
            enrollment.delete()
            barbellclass.available_spots += 1
            barbellclass.save()
        return redirect('my_barbellclasses')


def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})


def my_barbellclasses(request):
    context = {
        'my_barbellclasses': Enrollment.objects.filter(user=request.user)
    }
    return render(request, 'barbell_classes/my_barbellclasses.html', context)


@csrf_exempt
def barbellclass_list_json(request):
    classes = BarbellClass.objects.all()
    events = []
    for barbell_class in classes:
        events.append({
            'id': barbell_class.id,
            'title': barbell_class.title,
            'start': barbell_class.class_datetime.isoformat(),
        })
    return JsonResponse(events, safe=False)