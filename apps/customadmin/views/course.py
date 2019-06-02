from django.views import View
from django.views.generic import (
    DetailView,ListView
)
from django.views.generic.edit import (
    
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from apps.management.models import Course

class CourseListView(ListView):
    model = Course
    template_name = 'my_admin/management/course/list.html'