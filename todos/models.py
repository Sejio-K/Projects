from django.db import models
from datetime import date
from django.contrib.auth.models import User

class Label(models.Model):
    label_name = models.CharField(max_length=100)
    def __str__(self):
        return self.label_name
class Priority(models.Model):

  PRIORITY_CHOICES = (
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low')
  )

class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    labels = models.ManyToManyField(Label, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, default=3)
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


