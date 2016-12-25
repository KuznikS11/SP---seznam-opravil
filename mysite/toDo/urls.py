from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^profil/(?P<user_id>[0-9]+)/$', views.profil, name='profil'),
    url(r'^allTasks/(?P<user_id>[0-9]+)/$', views.allTasks, name='allTasks'),
    url(r'^editTask/(?P<task_id>[0-9]+)/$', views.editTask, name='editTask'),
    url(r'^newTask/', views.newTask, name='newTask'),
    url(r'^logout/', views.logout_user, name='logout'),
]
