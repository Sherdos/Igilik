

from freelance.models import Media
from rest_framework.response import Response
from rest_framework.decorators import action




class MediaMixin():

    @action(methods=['get'], detail=True)
    def image(self, request, pk = None):
        images = Media.objects.filter(obj=pk)
        images_list = []
        for i in images:
            images_list.append(i.image.url)
        return Response({'images':images_list})
    
# def f(obj):
#     service = obj.objects.get(id=model.data['id'])
#     media = Media.objects.create(obj_id = service.id, image = images)