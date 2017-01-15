from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, EditTaskForm, NewTaskForm, ChooseTasksForm, RegisterForm, SettingsForm
from .models import Task, User

from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta

def index(request):
    context = {}
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                login(request, user)
                return home(request)
            else:
                context['login_message'] = 'Your username or password is incorrect! Enter the username and password correctly!'

    context['login_form'] = LoginForm()
    
    return render(request,'toDo/index.html', context)

@login_required
def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))

def login_my(request):
    context = {}
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                login(request, user)
                return home(request)
            else:
                context['login_message'] = 'Your username or password is incorrect! Enter the username and password correctly!'
                

    context['login_form'] = LoginForm()
    
    return render(request,'toDo/login.html', context)

def register(request):
    context = {'register_form': RegisterForm()}

    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.p1_p2_same()
            user = User.objects.create_user(username=form.cleaned_data['username'],password=password)
            user.save()
            return HttpResponseRedirect(reverse('login_my'))
            
    return render(request,'toDo/register.html', context)

@login_required
def home(request):
    return HttpResponseRedirect(reverse('profil', args=[request.user.id]))

@login_required
def profil(request, user_id):
    context = {}
    context['user_id'] = user_id

    context['n_finished'] = len(Task.objects.filter(id_user=user_id, finished = True))
    context['n_unfinished'] = len(Task.objects.filter(id_user=user_id, finished = False))
    
    all_tasks = Task.objects.filter(id_user=user_id, finished = False)
    if len(all_tasks) > 9:
        all_tasks = all_tasks[:9]
    context['all_tasks'] = all_tasks

    if len(all_tasks) <=3:
        important_tasks = all_tasks
    else:
        important_tasks = all_tasks.order_by('due_date')[:3]
    context['important_tasks'] = important_tasks
    
    return render(request,'toDo/profil.html', context)

    

@login_required
def allTasks(request, user_id):
    context = {}
    if request.GET:
        form = ChooseTasksForm(data=request.GET)
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

@login_required
def editTask(request, task_id):
    context = {}
    t = Task.objects.get(pk=task_id)
    context['task'] = t

    etForm = EditTaskForm(instance=t)
    if request.method == "POST":
        etForm = EditTaskForm(request.POST, instance=t)
        if etForm.is_valid():
            etForm.save()
            return HttpResponseRedirect(reverse('allTasks', args=[request.user.id]))

    context['edit_task_form'] = etForm
    
    return render(request,'toDo/editTask.html', context)

@login_required
def newTask(request, user_id):
    context = {'new_task_form': NewTaskForm()}

    if request.method=='POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(name=form.cleaned_data['name'], due_date=form.cleaned_data['due_date'], description=form.cleaned_data['description'],
                                       category=form.cleaned_data['category'], priority=form.cleaned_data['priority'], id_user = User.objects.get(pk=user_id))
            task.save()
            return HttpResponseRedirect(reverse('allTasks', args=[request.user.id]))
    
    return render(request, 'toDo/newTask.html', context)

@login_required
def settings(request, user_id):
    context = {'settings_form' : SettingsForm()}
    if request.method=='POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.p1_p2_same()
            user = User.objects.get(pk=user_id)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                context['message'] = 'You enter the wrong old password!'
            
    return render(request, 'toDo/settings.html', context)


@login_required
def done(request, task_id):
    t = Task.objects.get(pk=task_id)
    t.finished = True
    t.save()
    
    return HttpResponseRedirect(reverse('profil', args=[request.user.id]))

@login_required
def delete_account(request, user_id):
    u = User.objects.get(pk=user_id)
    u.delete()
    
    return HttpResponseRedirect(reverse('index'))

def legal(request):
    return render(request, 'toDo/legal.html')

