from django.contrib import admin
from .models import Note, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tagid','name']
    search_fields = ['name']
    
    
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['noteid', 'title', 'content', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    filter_horizontal = ['tags']
