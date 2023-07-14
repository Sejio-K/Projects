from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm, TodoUpdateForm
from .models import Todo
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required


@csrf_exempt
def todos(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_obj = form.save()
            return JsonResponse({'todo': model_to_dict(todo_obj)})
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})
    todos_data = [model_to_dict(todo) for todo in Todo.objects.all()]
    return JsonResponse({'todos': todos_data})

@csrf_exempt
def todo(request, todo_id):
    try:
        todo_obj = Todo.objects.get(id = todo_id)
    except Exception:
        return JsonResponse({'status': 404, 'errors': 'Post not found.'})
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo_obj)
        if form.is_valid():
            todo_obj = form.save()
            return JsonResponse({'todo': model_to_dict(todo_obj)})
        else:
            return JsonResponse({'status': 400, 'errors': form.errors})
    elif request.method == 'DELETE':
        todo_obj.delete()
        return JsonResponse({'status': 204, 'message': 'Todo successfully deleted'})
    return JsonResponse({'todo': model_to_dict(todo_obj)})


