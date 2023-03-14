from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone,dateformat
# Create your models here.

class Employee (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False,max_length=50)
    firstName = models.CharField(name='first_name',max_length=50)
    lastName = models.CharField(name='last_name',max_length=50)
    username = models.CharField(name='username',max_length=50)
    national_id_number = models.IntegerField (name='id_no')
    # address =
    # phone_number =

class Task(models.Model):
    status_task = (
        ('At Site','At Site'),
        ('Remote', 'Remote')
    )

    title = models.CharField(max_length = 50)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=False,default='')
    date = models.DateField(verbose_name='تاریخ')
    is_remote =  models.BooleanField(default='At Site',choices=status_task,verbose_name='دورکاری')
    time_start = models.TimeField(default=timezone.now,verbose_name='زمان شروع',null=False)
    time_end = models.TimeField(default=timezone.now,verbose_name='زمان پایان',null=False)
    description = models.TextField(max_length=100,verbose_name='توضیحات')
    created_at = models.DateTimeField(auto_now_add=True)
