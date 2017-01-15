from django import forms
from .models import Task

class LoginForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password = forms.CharField(label='Password:', max_length=100, widget=forms.PasswordInput)


class EditTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'due_date', 'description', 'category', 'priority', 'finished']

class NewTaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'due_date', 'description', 'category', 'priority']

class ChooseTasksForm(forms.Form):
  old_new = forms.ChoiceField(label='Which tasks', choices=(('1', 'Unfinished'), ('2', 'Finished')), initial= '1')
  sort = forms.ChoiceField(label='Sort by',choices=(('1', 'By Date'), ('2', 'By Category'), ('3', 'By Priority')), initial= '1')

class RegisterForm(forms.Form):
  username = forms.CharField(label='Username:', max_length=100)
  password1 = forms.CharField(label='Password:', max_length=100, widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirm Password:', max_length=100, widget=forms.PasswordInput)

  def p1_p2_same(self):
    password1 = self.cleaned_data['password1']
    password2 = self.cleaned_data['password2']
    if password1 == password2:
      return password1
    else:
      raise forms.ValidationError('Passwords do not match.')


class SettingsForm(forms.Form):
  old_password = forms.CharField(label='Old Password:', max_length=100, widget=forms.PasswordInput)
  password1 = forms.CharField(label='New Password:', max_length=100, widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirm new Password:', max_length=100, widget=forms.PasswordInput)

  def p1_p2_same(self):
    password1 = self.cleaned_data['password1']
    password2 = self.cleaned_data['password2']
    if password1 == password2:
      return password1
    else:
      raise forms.ValidationError('Passwords do not match.')
  
  
  
