from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Task(models.Model):
    PRIORITY = ((i,i) for i in range(1,11))
    
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField( default=datetime.now )
    description = models.TextField()
    category = models.CharField(max_length=100)
    priority = models.IntegerField(choices = PRIORITY)
    finished = models.BooleanField(default=False)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
