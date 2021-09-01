from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import os

class ResultCategory(models.Model):
    resultcategory = models.CharField(max_length=50)
    def __str__(self):
        return '<' + str(self.resultcategory) + '>'
    class Meta:
        ordering = ('resultcategory',)

class TaskCategory(models.Model):
    taskcategory = models.CharField(max_length=50)
    def __str__(self):
        return '<' + str(self.taskcategory) + '>'
    class Meta:
        ordering=('taskcategory',)

class Item(models.Model):
    itemname = models.CharField(max_length=100)
    def __str__(self):
        return '<' + str(self.itemname) + '>'
    class Meta:
        ordering = ('itemname',)

class Grade(models.Model):
    gradename = models.CharField(max_length=100)
    def __str__(self):
        return '<' + str(self.gradename) + '>'
    class Meta:
        ordering = ('gradename',)

class Task(models.Model):
    taskcategory = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    tasknum = models.CharField(max_length=20)
    lot = models.CharField(max_length=20, null=True, blank=True)
    impdate = models.DateField(default=timezone.now, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True, blank=True)
    itemsize = models.IntegerField(default=0)
    taskdate = models.DateField(default=timezone.now, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.taskcategory) + '-<' + str(self.tasknum) + '>'
    class Meta:
        ordering = ('-tasknum',)

#def get_profileImage_file_path(instance, filename):
#    return os.path.join('%s/uploadedPhotos/profileImages' % instance.user_id, filename)

class Inspection(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    resultcategory = models.ForeignKey(ResultCategory, on_delete=models.CASCADE, null=True, blank=True,)
    picpath = models.CharField(max_length=200, null=True, blank=True,)
    #originalpic = models.ImageField(upload_to='', null=True, blank=True,  default='/static/img/original.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '<' + str(self.id) + '>'
    class Meta:
        ordering =('-id',)

class PicRecord(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE, null=True, blank=True)
    x1 = models.IntegerField(default=0)
    y1 = models.IntegerField(default=0)
    x2 = models.IntegerField(default=0)
    y2 = models.IntegerField(default=0)
    gaus = models.IntegerField(default=1)
    thrh = models.IntegerField(default=0)
    #cutimage = models.ImageField(upload_to='', null=True, blank=True)
    def __str__(self):
        return '<' + str(self.inspection) + '>'
    class Meta:
        ordering = ('-id',)

