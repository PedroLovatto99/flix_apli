from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'