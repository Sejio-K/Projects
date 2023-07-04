import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json
from .models import Todo


def todos(request):
    todos = Todo.objects.all()
    return render(request, 'todos.html', {'todos': todos})

