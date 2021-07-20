from django.db import models

# Create your models here.
class TodoItems(models.Model):
    TodoTitle = models.TextField()
    TodoDate = models.CharField(max_length=20)