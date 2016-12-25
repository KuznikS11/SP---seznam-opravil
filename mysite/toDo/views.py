from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, EditTaskForm
from .models import Task

from django.contrib.auth.decorators import login_required

def index(request):
    context = {} 
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                context['user_id'] = request.user.id #ne dela!!!!
                login(request, user)


    context['login_form'] = LoginForm()
    
    return render(request,'toDo/index.html', context)

@login_required
def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def login(request):
    context = {}
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                login(request, user)
                

    context['login_form'] = LoginForm()
    
    return render(request,'toDo/login.html', context)

def register(request):
    return render(request,'toDo/register.html')

@login_required
def profil(request, user_id):
    return render(request,'toDo/profil.html', {'user_id' : user_id})

@login_required
def allTasks(request, user_id):
    t = Task.objects.filter(id_user=user_id)
    return render(request,'toDo/allTasks.html', {'tasks' : t})

@login_required
def editTask(request, task_id):
    context = {}
    t = Task.objects.get(pk=task_id)
    context['task'] = t

    etForm = EditTaskForm(instance=t)
    if request.method == "POST":
        etForm = EditTaskForm(request.POST, instance=a)
        if etForm.is_valid():
            etForm.save()

    context['edit_task_form'] = etForm
    
    return render(request,'toDo/editTask.html', context)

@login_required
def newTask(request):
    return render(request, 'toDo/newTask.html')
