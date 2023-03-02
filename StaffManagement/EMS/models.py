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
    date = models.DateField(verbose_name='تاریخ')
    is_remote = models.BooleanField(null=True) # request for remote work
    is_leave = models.BooleanField(null=True) # request for leave
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(verbose_name='تاریخ شروع')
    end_date = models.DateField(verbose_name='تاریخ پایان')

class Task(models.Model):
    title = models.CharField(max_length = 50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ')
    is_remote =  models.BooleanField(null=True,verbose_name='دورکاری')
    time_start = models.TimeField(verbose_name='زمان شروع',null=False,default='')
    time_end = models.TimeField(verbose_name='زمان پایان',null=False,default='')
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)

class Attendance (models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ')
    arrival_time = models.TimeField()
    leaving_time = models.TimeField()
    is_absent = models.BooleanField()
