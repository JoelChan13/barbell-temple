from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from .models import BarbellClass, Enrollment
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

# View for the home page
def home(request):
    context = {
        'barbellclass_updates': BarbellClass.objects.all()
    }
    return render(request, 'barbell_classes/home.html', context)

# List view for barbell classes
class BarbellClassListView(ListView):
    model = BarbellClass
    template_name = 'barbell_classes/home.html'
    context_object_name = 'barbellclass_updates'
    ordering = ['-date_posted']

# Detail view for a single barbell class
class BarbellClassDetailView(DetailView):
    model = BarbellClass

    # Additional context data for checking if the user is enrolled in the class
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

# View for creating a new barbell class
class BarbellClassCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

    # Assign the current user as the author of the class
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check if the user is staff or superuser
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    # Redirect to home page if the user doesn't have permission
    def handle_no_permission(self):
        return redirect('barbell_classes-home')

# View for updating an existing barbell class
class BarbellClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

    # Assign the current user as the author of the class
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Check if the user is the author of the class
    def test_func(self):
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    # Redirect to home page if the user doesn't have permission
    def handle_no_permission(self):
        return redirect('barbell_classes-home')

# View for deleting an existing barbell class
class BarbellClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BarbellClass
    success_url = "/"

    # Check if the user is the author of the class
    def test_func(self):
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    # Redirect to home page if the user doesn't have permission
    def handle_no_permission(self):
        return redirect('barbell_classes-home')

# View for enrolling in a barbell class
class BarbellClassEnrol(LoginRequiredMixin, View):
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        if barbellclass.available_spots > 0:
            Enrollment.objects.get_or_create(user=request.user, barbell_class=barbellclass)
            barbellclass.available_spots -= 1
            barbellclass.save()
        return redirect('my_barbellclasses')

# View for unenrolling from a barbell class
class BarbellClassUnenrol(LoginRequiredMixin, View):
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        enrollment = Enrollment.objects.filter(user=request.user, barbell_class=barbellclass)
        if enrollment.exists():
            enrollment.delete()
            barbellclass.available_spots += 1
            barbellclass.save()
        return redirect('my_barbellclasses')

# View for rendering the timetable page
def timetable(request):
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})

# View for rendering the page displaying user's enrolled barbell classes
def my_barbellclasses(request):
    context = {
        'my_barbellclasses': Enrollment.objects.filter(user=request.user)
    }
    return render(request, 'barbell_classes/my_barbellclasses.html', context)

# View for handling JSON data of barbell class list
@csrf_exempt
def barbellclass_list_json(request):
    # Retrieve all barbell classes
    classes = BarbellClass.objects.all()
    events = []
    # Convert barbell class objects to JSON format
    for barbell_class in classes:
        events.append({
            'id': barbell_class.id,
            'title': barbell_class.title,
            'start': barbell_class.class_datetime.isoformat(),
        })
    # Return JSON response
    return JsonResponse(events, safe=False)