from django.urls import path, include
from todos.views.todos import todos, create_todo, update_todo, delete_todo, complete_todo

urlpatterns = [
    path('', todos, name='todos'),
    path('create/', create_todo, name="create_todo"),
    path('update/<int:todo_id>/ ', update_todo, name="update_todo"),
    path('delete/<int:todo_id>/ ', delete_todo, name="delete_todo")

]
