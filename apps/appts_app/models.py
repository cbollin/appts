from __future__ import unicode_literals
from ..login_app.models import User, UserManager
from django.db import models
from time import strftime
from datetime import datetime, timedelta, date, time

# Create your models here.

class ApptManager(models.Manager):
    def add(self, data):
        errors = []
        today = strftime("%Y-%m-%d")
        now = strftime("%H-%M-%S")
        if data['date'] == "" or data['date'] < today:
            errors.append("Please enter a valid date")
        if data['date'] == today and data['time'] < now:
            errors.append("Please enter a valid time")
        if data['time'] == "":
            errors.append("Please enter a time")
        if len(data['task']) == 0:
            errors.append("Please enter a task")
        if errors:
            return(True, errors)
        else:
            return (False, data)

class Appt(models.Model):
    my_task = models.CharField(max_length=45)
    my_time = models.TimeField()
    my_date = models.DateField()
    my_status = models.CharField(max_length=10)
    user = models.ForeignKey('login_app.User', related_name='user')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    ApptManager = ApptManager()
    objects = models.Manager()
