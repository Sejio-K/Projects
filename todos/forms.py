from django import forms
from .models import Todo
from django.core.exceptions import ValidationError

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'body', 'user_id']