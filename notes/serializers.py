from rest_framework import serializers
from .models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tagid', 'name']
        

class NoteSerializer(serializers.ModelSerializer):
    # tags = serializers.ListField(child=serializers.CharField(), required=False)
    input_tags = serializers.ListField( child=serializers.CharField(), write_only=True, required=False )
    # output-only for GET
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Note
        fields = ['noteid', 'title', 'content','input_tags', 'tags']
        read_only_fields = ['created_at', 'updated_at']

    
    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]


    def create(self, validated_data):
        tags_data = validated_data.pop('input_tags', [])
        note = Note.objects.create(**validated_data)
        for tag_name in tags_data:
            tag_name = tag_name.strip()
            if tag_name:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                note.tags.add(tag)            
        return note
    
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('input_tags', None)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        if tags_data:
            instance.tags.clear()
            for tag_name in tags_data:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, _ = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)
        return instance
    
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['tags'] = [tag.name for tag in instance.tags.all() ]
    #     return data