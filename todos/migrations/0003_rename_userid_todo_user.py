# Generated by Django 4.2.1 on 2023-07-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todo_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='userId',
            new_name='User',
        ),
    ]