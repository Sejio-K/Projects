from django.urls import path
from todos.views.api import todo, todos

urlpatterns = [
    path('api/todos/', todos, name='todos'),
    path('api/todo/<int:todo_id>/', todo, name='todo'),
]
