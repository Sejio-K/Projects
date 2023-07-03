import datetime
import random
from django.contrib.auth.models import User

from .models import Todo

def create_initial_db():
    users_data = [
        {'username': 'fill', 'email': 'fill@gmail.com', 'password': '12345'},
        {'username': 'andrew', 'email': 'andrew@gmail.com', 'password': '12345'},
        {'username': 'olga', 'email': 'olga@gmail.com', 'password': '12345'},
        {'username': 'valeria', 'email': 'valeria@gmail.com', 'password': '12345'},
        {'username': 'tom', 'email': 'tom@gmail.com', 'password': '12345'},
    ]

    todos_data = [
        {'title': 'Task 1', 'body': 'This is task 1'},
        {'title': 'Task 2', 'body': 'This is task 2'},
        {'title': 'Task 3', 'body': 'This is task 3'},
        {'title': 'Task 4', 'body': 'This is task 4'},
        {'title': 'Task 5', 'body': 'This is task 5'},
    ]

    users = []
    todos = []

    for user_data, todo_data in zip(users_data, todos_data):
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password'],
            is_active=True
        )
        users.append(user)

        todo = Todo(
            user=user,
            title=todo_data['title'],
            body=todo_data['body']
        )
        todo.save()
        todos.append(todo)

    return users, todos
