from django.db import models



class Subscription(models.Model):
    student = models.ForeignKey(
        'management.Student',
        on_delete=models.CASCADE
    )
    cycle = models.ForeignKey(
        'management.Cycle',
        on_delete=models.CASCADE
    )

    registered_date = models.DateField()