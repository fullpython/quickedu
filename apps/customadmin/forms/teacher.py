from django.forms import ModelForm

from apps.management.models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name',
                  'middle_name', 'teachable_courses']
