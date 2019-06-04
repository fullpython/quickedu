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
from django.urls import reverse_lazy
class CourseListView(ListView):
    model = Course
    template_name = 'my_admin/management/course/list.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'my_admin/management/course/create.html'
    success_url = reverse_lazy('course_list')
    fields = ['name','description']


class CourseDetailView(DetailView):
    model = Course
    template_name = 'my_admin/management/course/detail.html'