import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
import json

class Todo:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

class Todos:
    def __init__(self):
        self.todos = []

    def fetch_data(self):
        # Список задач, которые вы хотите отобразить
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        if response.status_code == 200:
            # Декодировать данные в формате JSON
            todo_data = response.json()
            self.todos = [Todo(data ['userId'], data['id'], data['title'], data['body']) for data in todo_data]
        else:
            self.todos = []

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
        todos.todos = [Todo(data ['userId'], data['id'], data['title'], data['body']) for data in todo_data]
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

def add_todo(request):
    if request.method == 'POST':
        task = request.POST.dict()
        task['title'] = str(task['title'])
        task['body'] = str(task['body'])
        task['userId'] = str(task['userId'])
        task['id'] = str(task['id'])
        todos = Todos()
        todos.fetch_data()

        todo = Todo(task['userId'], task['id'], task['title'], task['body'])
        todos.todos.append(todo)

        json_todo = todos.to_json()

        return render(request, 'todos/home.html', {'todos': json_todo})

    return render(request, 'create_todo.html')
