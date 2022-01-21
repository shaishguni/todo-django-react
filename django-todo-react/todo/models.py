from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    completed = models.BooleanField(default=False)
