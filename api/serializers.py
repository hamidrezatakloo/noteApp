from rest_framework import serializers
from .models import TodoItem, Note, TodoList


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'


class TodoListSerializer(serializers.ModelSerializer):
    items = TodoItemSerializer(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ['id', 'name', 'created_at', 'items']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
