from django.db import models


class Tag(models.Model):
    tagid = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    
class Note(models.Model):
    noteid = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title