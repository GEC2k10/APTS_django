from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
projects=((1,'Mini'),(2,'Main'))
class Project(models.Model):
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    active=models.BooleanField(default=True)
    year=models.IntegerField()
    ptype=models.IntegerField(choices=projects,verbose_name='Project Type')
    def __unicode__(self):
        return self.name

class Guide(models.Model):
    user=models.ForeignKey(User)
    project=models.ManyToManyField(Project)
    def __unicode__(self):
        return self.user.username

class Commit(models.Model):
    project=models.ForeignKey(Project)
    dialogue=models.CharField(max_length=100)
    commit=models.CharField(max_length=8)
    def __unicode__(self):
        return self.commit

admin.site.register(Guide)
admin.site.register(Commit)
admin.site.register(Project)
