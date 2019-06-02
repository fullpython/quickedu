from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30)

    date_of_birth = models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
