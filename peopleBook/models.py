from django.db import models

class People(models.Model):
    name = models.CharField(max_length=255)
    job = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Create your models here.
