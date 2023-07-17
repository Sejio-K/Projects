from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from todos.forms import TodoForm, TodoUpdateForm
from todos.models import Todo
from django.forms.models import model_to_dict
from django.http import JsonResponse

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
    todo_obj = get_object_or_404(Todo, id=todo_id)
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
