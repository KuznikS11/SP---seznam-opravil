from django import forms
from .models import Task

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password = forms.CharField(label='Password:', max_length=100, widget=forms.PasswordInput)


class EditTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'due_date', 'description', 'category', 'priority', 'finished']

class ChooseTasksForm(forms.Form):
  old_new = forms.ChoiceField(label='Which tasks', choices=(('1', 'Unfinished'), ('2', 'Finished')), initial= '1')
  sort = forms.ChoiceField(label='Sort by',choices=(('1', 'By Date'), ('2', 'By Category'), ('3', 'By Priority')), initial= '1')
