# Generated by Django 4.2.1 on 2023-07-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_rename_userid_todo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='User',
            new_name='user',
        ),
    ]