from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from todos.forms import TodoForm, TodoUpdateForm
from todos.models import Todo
from django.forms.models import model_to_dict
from django.http import JsonResponse


def todos(request):
    return render(request, 'todos.html', {'todos': Todo.objects.all()})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
        else:
            return render(request, "create_todo.html", {"form": form})
    return render(request, "create_todo.html", {"form": TodoForm()})
def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
    return render(request, 'update_todo.html', {"form": form})

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('todos')