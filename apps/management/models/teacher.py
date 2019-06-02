from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


    teachable_courses = models.ManyToManyField(
        'management.Course'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'