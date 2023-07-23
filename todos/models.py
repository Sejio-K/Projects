from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Label(models.Model):
    label_name = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return self.label_name

class Priority(models.Model):

    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    name = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')

    def __str__(self):
        return self.name
class Todo(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    label = models.ManyToManyField(Label, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todos')
    parent_task = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


def assign_priority_values():
    # Проверяем, есть ли уже значения приоритетов в модели
    if Priority.objects.exists():
        print("Приоритеты уже добавлены.")
        return

    # Значения приоритетов для добавления
    priority_values = ['Low', 'Medium', 'High']

    # Создаем объекты Priority и сохраняем их в базу данных
    for priority_value in priority_values:
        priority = Priority(name=priority_value)
        priority.save()

    print("Значения приоритетов успешно добавлены.")

def assign_label_values():
    # Проверяем, есть ли уже значения меток в модели
    if Label.objects.exists():
        print("Метки уже добавлены.")
        return

    # Значения меток для добавления
    label_values = ['Label 1', 'Label 2', 'Label 3']

    # Создаем объекты Label и сохраняем их в базу данных
    for label_value in label_values:
        label = Label(label_name=label_value)
        label.save()

    print("Метки успешно добавлены.")