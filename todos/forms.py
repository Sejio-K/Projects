from django import forms
from .models import Todo, Label, Priority
from django.core.exceptions import ValidationError

class TodoForm(forms.ModelForm):

    label = forms.ModelMultipleChoiceField(queryset=Label.objects.all(), widget=forms.CheckboxSelectMultiple)
    priority = forms.ModelChoiceField(queryset=Priority.objects.all())
    parent_task = forms.ModelChoiceField(queryset=Todo.objects.all(), required=False)

    # остальной код формы


    class Meta:
        model = Todo
        fields = ['title', 'body', 'parent_task', 'user', 'completed', 'label',  'priority', 'parent_task']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['label'].widget = forms.SelectMultiple(attrs={'class': 'form-control'})
        self.fields['label'].queryset = Label.objects.all()
    def clean_title(self):  # проверка title на длинну
        if len(self.cleaned_data.get('title')) < 2:
            raise ValidationError('Value must be more then 1 character.')
        return self.cleaned_data.get('title')

class TodoUpdateForm(TodoForm):
    title = forms.CharField(required=False)
    body = forms.CharField(required=False)
    completed = forms.CharField(required=False, initial=0) # initial - значение с которым идет изначально

    class Meta:
        model = Todo
        fields = ['title', 'body', 'user', 'completed']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data.get('title') or self.instance.title
        cleaned_data['body'] = cleaned_data.get('body') or self.instance.body
        cleaned_data['user'] = cleaned_data.get('user') or self.instance.user
        cleaned_data['completed'] = cleaned_data.get('completed') if cleaned_data.get(
            'completed') is not None else self.instance.completed

    def clean_body(self):
        return self.cleaned_data.get('body').replace('/', '').strip()
