from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_date = models.DateField(default=date.today)
    user_id = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
