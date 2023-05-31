import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json

class Todo:
    def __init__(self, id, title, completed):
        self.id = id
        self.title = title
        self.completed = completed

class Todos:
    def __init__(self):
        self.todos = []

    def fetch_data(self):
        # Список задач, которые вы хотите отобразить
        custom_todos = [
            {"id": 1, "title": "Задача 1", "completed": False},
            {"id": 2, "title": "Задача 2", "completed": True},
            {"id": 3, "title": "Задача 3", "completed": False}
        ]
        self.todos = [Todo(data['id'], data['title'], data['completed']) for data in custom_todos]

    def __iter__(self):
        return iter(self.todos)

    def get_todo_by_id(self, todo_id):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def to_json(self):
        return json.dumps([todo.__dict__ for todo in self.todos])

    @classmethod
    def from_json(cls, json_data):
        todos = cls()
        todo_data = json.loads(json_data)
        todos.todos = [Todo(data['id'], data['title'], data['completed']) for data in todo_data]
        return todos


class TodoListView(View):
    def get(self, request):
        todos = Todos()
        todos.fetch_data()
        return render(request, 'todos/home.html', {'todos': todos})


class TodoJSONView(View):
    def get(self, request):
        todos = Todos()
        todos.fetch_data()
        return JsonResponse(todos.to_json(), safe=False)
