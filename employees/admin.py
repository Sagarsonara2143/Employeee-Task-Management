from django.contrib import admin
from .models import Employee, Task

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empid', 'name', 'email', 'department', 'date_joined']
    # search_fields = ['name', 'email', 'department']
    search_fields = []
    list_filter = []


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['taskid', 'title', 'description', 'due_date', 'status', 'assigned_to', 'completed_date']
    list_filter = ['status', 'assigned_to']
    search_fields = ['title', 'description']