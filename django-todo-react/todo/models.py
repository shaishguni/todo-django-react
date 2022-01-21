from django.db import models

# Create your models here.

class Todo(models.model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    done = models.BooleanField(default=False)
