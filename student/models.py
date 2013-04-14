from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from guide.models import Project

class Student(models.Model):
    user=models.ForeignKey(User)
    project=models.ForeignKey(Project)
    def __unicode__(self):
        return user.username

admin.site.register(Student)
