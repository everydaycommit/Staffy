from django.contrib import admin
from Core.models import Task,Employee
# Register your models here.

# admin.site.register(Task)
# admin.site.register(Employee)

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ('username','user')
    list_filter = ('first_name','last_name','username')
    search_fields = ('is_remote','time_start','time_end','description','created_at')

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('title','employee','date','is_remote','description')
    list_filter = ('title','employee','date','is_remote')
    search_fields = ('title','employee','date','is_remote','time_start','time_end','description','created_at')