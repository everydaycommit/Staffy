from django.contrib import admin
from Core.models import Task,Employee
# Register your models here.

# admin.site.register(Task)
# admin.site.register(Employee)

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['title','employee','date','is_remote','time_start','time_end','description']
    list_filter = ['title','employee','date','is_remote']
    search_fields = ['title','employee','date','is_remote','time_start','time_end','description','created_at']
    raw_id_fields = ['title','employee']
    date_hierarchy =['created_at']
    ordering = ['At site','Remote']

@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ['title','employee','date','is_remote','time_start','time_end','description']
    list_filter = ['title','employee','date','is_remote']
    search_fields = ['title','employee','date','is_remote','time_start','time_end','description','created_at']
    raw_id_fields = ['title','employee']
    date_hierarchy =['created_at']
    ordering = ['At site','Remote']
