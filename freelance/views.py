from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsServiceUserOrReadOnly
from .serialaizers import SerializerService
from .models import Service,Media

# Create your views here.
class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = SerializerService
    permission_classes=(IsServiceUserOrReadOnly,)
    
   
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Service.objects.all()[:2]
        return Service.objects.filter(pk=pk)
    
    def create(self, request, *args, **kwargs):
        images =request.data['images']
        del request.data['images']
        model=super().create(request, *args, **kwargs)
        service = Service.objects.get(id=model.data['id'])
        media = Media.objects.create(obj_id = service.id, image = images)
        return model
    
    
    
    @action(methods=['get'], detail=True)
    def user(self, request, pk = None):
        service = Service.objects.get(pk=pk)
        return Response({'users':service.user.username})
    
    @action(methods=['get'], detail=True)
    def image(self, request, pk = None):
        images = Media.objects.filter(service_id=pk)
        images_list = []
        for i in images:
            images_list.append(i.image.url)
        return Response({'images':images_list})