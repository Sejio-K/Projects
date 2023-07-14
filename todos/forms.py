from django import forms
from .models import Todo
from django.core.exceptions import ValidationError


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body', 'user_id', 'completed']

    def clean_title(self):  # проверка title на длинну
        if len(self.cleaned_data.get('title')) < 2:
            raise ValidationError('Value must be more then 1 character.')
        return self.cleaned_data.get('title')

class TodoUpdateForm(TodoForm):
    title = forms.CharField(required=False)
    body = forms.CharField(required=False)
    completed = forms.CharField(required=False)

    class Meta:
        model = Todo
        fields = ['title', 'body', 'user_id', 'completed']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data.get('title') or self.instance.title
        cleaned_data['body'] = cleaned_data.get('body') or self.instance.body
        cleaned_data['user_id'] = cleaned_data.get('user_id') or self.instance.user_id
        cleaned_data['completed'] = cleaned_data.get('completed') if cleaned_data.get(
            'completed') is not None else self.instance.completed

    def clean_body(self):
        return self.cleaned_data.get('body').replace('/', '').strip()
