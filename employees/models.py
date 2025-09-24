from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Employee(models.Model):
    empid = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name + " - " + self.department 
    
    def clean(self):
        if self.date_joined > timezone.now().date():
            raise ValidationError("Date joined cannot be in the future.")
    

class Task(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    taskid = models.AutoField(primary_key=True, unique=True)    
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')
    completed_date = models.DateField(null=True, blank=True)

    
    def clean(self):
        if self.due_date < timezone.now().date():
            raise ValidationError("Due date cannot be in the past.")
    
    
    def save(self, *args, **kwargs):
        if self.status == "Completed" and not self.completed_date:
            self.completed_date = timezone.now().date()
        if self.status != "Completed" and self.completed_date:
            self.completed_date = None
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return f"{self.title} ({self.status})"