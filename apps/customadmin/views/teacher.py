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
from django.urls import reverse_lazy
from apps.management.models import Teacher

from apps.customadmin.forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher
    template_name = 'my_admin/management/teacher/list.html'

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'my_admin/management/teacher/create.html'
    success_url = reverse_lazy('teacher_list')
    form_class = TeacherForm
    
