from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,max_length=50)
    firstName = models.CharField(name='first_name',max_length=50)
    lastName = models.CharField(name='last_name',max_length=50)
    username = models.CharField(name='username',max_length=50)
    national_id_number = models.IntegerField (name='id_no')
    # address = 
    # phone_number = 

class Request (models.Model): 
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    title = models.CharField(max_length = 50)
    dayoff_from_date = models.DateField(verbose_name='تاریخ شروع مرخصی')
    dayoff_to_date = models.DateField(verbose_name='تاریخ پایان مرخصی')
    is_remote =  models.BooleanField(null=True) # request for remote work
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    title = models.CharField(max_length = 50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ')
    is_remote =  models.BooleanField(null=True,verbose_name='دورکاری')
    time_start = models.TimeField(verbose_name='زمان شروع',null=False,default='')
    time_end = models.TimeField(verbose_name='زمان پایان',null=False,default='')
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)

class Meeting(models.Model):
    title = models.CharField(max_length = 50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ جلسه')
    is_remote =  models.BooleanField(null=True,verbose_name='دورکاری')
    time_start = models.TimeField(verbose_name='زمان شروع جلسه',null=False,default='')
    time_end = models.TimeField(verbose_name='زمان پایان جلسه',null=False,default='')
    description = models.TextField(max_length=100,verbose_name='توضیحات جلسه')
    created_at = models.DateTimeField(auto_now_add=True)