from django import forms
from .models import Task

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password = forms.CharField(label='Password:', max_length=100, widget=forms.PasswordInput)


class EditTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'due_date', 'description', 'category', 'priority', 'finished']
