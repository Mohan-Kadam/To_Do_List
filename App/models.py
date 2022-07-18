from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    Task = models.CharField(max_length=18)
    Create_date = models.DateField(default=timezone.now)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Task

    def show_status(self):
        return self.Status