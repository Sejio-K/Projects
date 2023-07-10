from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
from .models import Todo
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


@csrf_exempt
def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return JsonResponse({'todo': model_to_dict(todo)})
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})
    todos = [model_to_dict(todo) for todo in Todo.objects.all()]
    return render(request, 'todos.html', {'todos': todos})


def view_todo(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id = todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Post not found.'})
    return JsonResponse({'todo': model_to_dict(todo_obj)})
