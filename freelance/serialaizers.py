from rest_framework import serializers
from .models import Service, Order



class SerializerService(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = serializers.ImageField(required=False)
    
    class Meta:
        model = Service
        fields = '__all__'


class SerializerOrder(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # images = serializers.ImageField(required=False)
    class Meta:
        model = Order
        fields = '__all__'
        

        
    