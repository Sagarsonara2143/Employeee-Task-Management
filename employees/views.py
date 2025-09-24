from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import EmployeeSerializer, TaskSerializer
from .models import Employee, Task
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['empid','name', 'email', 'department']
    search_fields = ['empid','name', 'email', 'department']

    
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('assigned_to').all().order_by('taskid')
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'assigned_to']
    search_fields = ['title', 'description']