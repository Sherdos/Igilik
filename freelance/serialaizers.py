from rest_framework import serializers
from .models import Service



class SerializerService(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = serializers.ImageField(required=False)
    
    class Meta:
        model = Service
        fields = '__all__'
        

        
    