from django.contrib import admin
from .models import Employee,Request,Task,User

# Register your models here.

admin.site.register(Employee)
admin.site.register(Request)
admin.site.register(Task)