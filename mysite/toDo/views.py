from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm

def index(request):
    context = {}
    
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'] )
            if user is not None:
                login(request, user)

    context['login_form'] = LoginForm()
    
    return render(request,'toDo/index.html', context)

def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('index'))
