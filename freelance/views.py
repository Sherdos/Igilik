from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsServiceUserOrReadOnly
from .serialaizers import SerializerService, SerializerOrder
from .models import Service,Media, Order

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerService
    permission_classes=(IsServiceUserOrReadOnly,)
    
   
    def create(self, request, *args, **kwargs):
        images =request.data['images']
        del request.data['images']
        model=super().create(request, *args, **kwargs)
        return model
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Service.objects.all()[:2]
        return Service.objects.filter(pk=pk)
    

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerOrder
    queryset = Order.objects.all()