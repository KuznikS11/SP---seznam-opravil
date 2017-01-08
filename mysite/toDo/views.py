from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, EditTaskForm, ChooseTasksForm
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


def profil(request, user_id):
    context = {}
    context['user_id'] = user_id

    context['n_finished'] = len(Task.objects.filter(finished = True))
    context['n_unfinished'] = len(Task.objects.filter(finished = False))
    
    all_tasks = Task.objects.filter(id_user=user_id)
    if len(all_tasks) > 9:
        all_tasks = all_tasks[:9]
    context['all_tasks'] = all_tasks

    if len(all_tasks) <=3:
        important_tasks = all_tasks
    else:
        important_tasks = all_tasks.order_by('due_date')[:3]
    context['important_tasks'] = important_tasks
    return render(request,'toDo/profil.html', context)


def allTasks(request, user_id):
    context = {}
    if request.GET:
        form = ChooseTasksForm(data=request.GET)
        print(form.is_valid(), form.errors)
        if form.is_valid():
            old_new_f = form.cleaned_data['old_new']
            sort_f = form.cleaned_data['sort']
            if old_new_f == '1':
                t = Task.objects.filter(id_user=user_id, finished=False)
            else:
                t = Task.objects.filter(id_user=user_id, finished=True)

            if sort_f == '1':
                t = t.order_by('due_date')

            if sort_f == '2':
                t = t.order_by('category')

            if sort_f == '3':
                t = t.order_by('-priority')

            

            context['tasks'] = t

    context['choose_tasks_form'] = ChooseTasksForm()

        
    return render(request,'toDo/allTasks.html', context)


def editTask(request, task_id):
    context = {}
    t = Task.objects.get(pk=task_id)
    context['task'] = t

    etForm = EditTaskForm(instance=t)
    if request.method == "POST":
        etForm = EditTaskForm(request.POST, instance=t)
        if etForm.is_valid():
            etForm.save()
            return HttpResponseRedirect(reverse('index'))

    context['edit_task_form'] = etForm
    
    return render(request,'toDo/editTask.html', context)

@login_required
def newTask(request):
    return render(request, 'toDo/newTask.html')
