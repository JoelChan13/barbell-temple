from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from .models import BarbellClass, Enrollment
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.urls import reverse

def home(request):
    """View for the home page"""
    context = {
        'barbellclass_updates': BarbellClass.objects.all()
    }
    return render(request, 'barbell_classes/home.html', context)

class BarbellClassListView(ListView):
    """List view for barbell classes"""
    model = BarbellClass
    template_name = 'barbell_classes/home.html'
    context_object_name = 'barbellclass_updates'
    ordering = ['-date_posted']

class BarbellClassDetailView(DetailView):
    """Detail view for a single barbell class"""
    model = BarbellClass

    def get_context_data(self, **kwargs):
        """Additional context data for checking if the user is enrolled in the class"""
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
    """View for creating a new barbell class"""
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

    def form_valid(self, form):
        """Assign the current user as the author of the class"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Check if the user is staff or superuser"""
        return self.request.user.is_staff or self.request.user.is_superuser

    def handle_no_permission(self):
        """Redirect to home page if the user doesn't have permission"""
        return redirect('barbell_classes-home')

class BarbellClassUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for updating an existing barbell class"""
    model = BarbellClass
    fields = ['title', 'class_datetime', 'duration', 'difficulty', 'description', 'available_spots']

    def form_valid(self, form):
        """Assign the current user as the author of the class"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Check if the user is the author of the class"""
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    def handle_no_permission(self):
        """Redirect to home page if the user doesn't have permission"""
        return redirect('barbell_classes-home')

class BarbellClassDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting an existing barbell class"""
    model = BarbellClass
    success_url = "/"

    def test_func(self):
        """Check if the user is the author of the class"""
        barbellclass = self.get_object()
        return self.request.user == barbellclass.author

    def handle_no_permission(self):
        """Redirect to home page if the user doesn't have permission"""
        return redirect('barbell_classes-home')

class BarbellClassEnrol(LoginRequiredMixin, View):
    """View for enrolling in a barbell class"""
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        if barbellclass.available_spots > 0:
            Enrollment.objects.get_or_create(user=request.user, barbell_class=barbellclass)
            barbellclass.available_spots -= 1
            barbellclass.save()
        return redirect('my_barbellclasses')

class BarbellClassUnenrol(LoginRequiredMixin, View):
    """View for unenrolling from a barbell class"""
    def post(self, request, pk):
        barbellclass = get_object_or_404(BarbellClass, pk=pk)
        enrollment = Enrollment.objects.filter(user=request.user, barbell_class=barbellclass)
        if enrollment.exists():
            enrollment.delete()
            barbellclass.available_spots += 1
            barbellclass.save()
        return redirect('my_barbellclasses')

def timetable(request):
    """View for rendering the timetable page"""
    return render(request, 'barbell_classes/timetable.html', {'title': 'Timetable'})

def my_barbellclasses(request):
    """View for rendering the page displaying user's enrolled barbell classes"""
    context = {
        'my_barbellclasses': Enrollment.objects.filter(user=request.user)
    }
    return render(request, 'barbell_classes/my_barbellclasses.html', context)

"""View for handling JSON data of barbell class list"""
@csrf_exempt
def barbellclass_list_json(request):
    """Retrieve all barbell classes"""
    classes = BarbellClass.objects.all()
    events = []
    """Convert barbell class objects to JSON format"""
    for barbell_class in classes:
        events.append({
            'id': barbell_class.id,
            'title': barbell_class.title,
            'start': barbell_class.class_datetime.isoformat(),
        })
    """Return JSON response"""
    return JsonResponse(events, safe=False)

class BarbellClassAuthorView(ListView):
    """View for displaying classes created by a specific author"""
    model = BarbellClass
    template_name = 'barbell_classes/author_classes.html'
    context_object_name = 'barbellclass_updates'

    def get_queryset(self):
        """Filter the BarbellClass objects by the author"""
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return BarbellClass.objects.filter(author=author).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        """Add additional context data to the template"""
        context = super().get_context_data(**kwargs)
        context['author'] = get_object_or_404(User, username=self.kwargs.get('username'))
        return context