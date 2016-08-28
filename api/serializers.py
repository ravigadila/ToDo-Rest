from django.contrib.auth.models import User
from rest_framework import serializers
from todo.models import List, Item


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('name', 'owner')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'list', 'created_date',
                  'due_date', 'completed', 'completed_date',
                  'created_by', 'assigned_to', 'note', 'priority')
