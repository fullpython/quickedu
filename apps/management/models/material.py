from django.db import models


class Material(models.Model):
    

    name = models.CharField(max_length=130)
    document = models.FileField(
        upload_to='materials/',
        null=True,
        blank=True
        )
    body = models.TextField(
        null=True,
        blank=True
    )
    cycle=models.ForeignKey(
        'management.Cycle',
        on_delete=models.CASCADE
    )