from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import NoteSerializer, TagSerializer
from .models import Note, Tag
from django.db.models import Q


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.prefetch_related('tags').all().order_by('noteid')
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.request.query_params.get('tag')
        search = self.request.query_params.get('search')
        if tag:
            queryset = queryset.filter(tags__name__iexact=tag)
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))
        return queryset.distinct()
    
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']