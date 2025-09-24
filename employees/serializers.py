from rest_framework import serializers
from .models import Employee, Task
from django.utils import timezone


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['empid', 'name', 'email', 'department', 'date_joined']
        
    def validate_date_joined(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Date joined cannot be in the future.")
        return value
    

   
class AssignedEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['empid', 'name']   

        
        
class TaskSerializer(serializers.ModelSerializer):
    assigned_to = AssignedEmployeeSerializer(read_only=True) 
    assigned_to_id = serializers.PrimaryKeyRelatedField( queryset=Employee.objects.all(), source='assigned_to', write_only=True )
    
    class Meta:
        model = Task
        fields = ['taskid', 'title', 'description', 'due_date', 'status', 'assigned_to', 'assigned_to_id', 'completed_date']        
        read_only_fields = ['completed_date']
        
        
    def validate_due_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

