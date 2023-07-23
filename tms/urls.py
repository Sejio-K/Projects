from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('todos.urls.api')),
    path('todos/', include('todos.urls.todos')),
]