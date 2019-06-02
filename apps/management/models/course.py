from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name