from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee (models.Model):
    user = models.ForeignKey(User,on_delete=True,max_length=50)
    first_name = models.CharField(name='first_name',max_length=50)
    last_name = models.CharField(name='last_name',max_length=50)
    username = models.CharField(name='last_name',max_length=50)
    national_id_number = models.IntegerField (name='id_no',max_length=10)
    # address = 
    # phone_number = 


class Performance (models.Model):
    arrive_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    leave_time = models.DateTimeField(auto_now_add=True,auto_created=True)
    attendance = models.DateTimeField(auto_now_add=True,auto_created=True)

class Request (models.Model): 
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    title = models.CharField(max_length = 50)
    date = models.DateField(verbose_name='تاریخ')
    is_remote =  models.BooleanField(null=True) # request for remote work
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)


class Employee_Finance (models.Model): 
    pass

class Task(models.Model):
    title = models.CharField(max_length = 50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ')
    is_remote =  models.BooleanField(null=True,verbose_name='دورکاری')
    time_start = models.TimeField(verbose_name='زمان شروع',null=False,default='')
    time_end = models.TimeField(verbose_name='زمان پایان',null=False,default='')
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)


class Team () : 
    pass 
