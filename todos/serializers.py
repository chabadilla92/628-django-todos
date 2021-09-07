from .models import Todo
from rest_framework import serializers 

## Create a Serializer for Our Model
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Todo
        fields = ['id', 'subject', 'details']

