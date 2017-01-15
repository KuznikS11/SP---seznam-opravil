from django.conf.urls import url
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^legal/', views.legal, name='legal'),
    url(r'^login_my/', views.login_my, name='login_my'),
    url(r'^register/', views.register, name='register'),
    url(r'^profiles/home', views.home, name='home'),
    url(r'^profil/(?P<user_id>[0-9]+)/$', views.profil, name='profil'),
    url(r'^allTasks/(?P<user_id>[0-9]+)/$', views.allTasks, name='allTasks'),
    url(r'^editTask/(?P<task_id>[0-9]+)/$', views.editTask, name='editTask'),
    url(r'^newTask/(?P<user_id>[0-9]+)/$', views.newTask, name='newTask'),
    url(r'^logout/', views.logout_user, name='logout_user'),
    url(r'^settings/(?P<user_id>[0-9]+)/$', views.settings, name='settings'),
    url(r'^done/(?P<task_id>[0-9]+)/$', views.done, name='done'),
    url(r'^delete_account/(?P<user_id>[0-9]+)/$', views.delete_account, name='delete_account'),
]
