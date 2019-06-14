from django.views import View
from django.views.generic import (
    DetailView, ListView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)
from django.urls import reverse_lazy
from apps.management.models import Course
from django.db.models import Q


class CourseListView(ListView):
    model = Course
    template_name = 'my_admin/management/course/list.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        query_name = self.request.GET.get('name', None)

        if query_name is not None:
            queryset = queryset.filter(
                Q(name__contains=query_name) | Q(
                    description__contains=query_name))
        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = 'my_admin/management/course/detail.html'


class CourseCreateView(CreateView):
    model = Course
    template_name = 'my_admin/management/course/create.html'
    success_url = reverse_lazy('course_list')
    fields = ['name', 'description']


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'my_admin/management/course/update.html'
    success_url = reverse_lazy('course_list')
    fields = ['name', 'description']


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'my_admin/management/course/delete.html'
    success_url = reverse_lazy('course_list')
