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
        title = request.POST.get('title')
        description = request.POST.get('description')

        # создаем новую задачу
        todo = Todo(id=10, title=title, completed=False)  # пример создания новой задачи
        todos = Todos()
        todos.todos.append(todo)

        return redirect('todo_list_view')

    return render(request, 'create_todo.html')
