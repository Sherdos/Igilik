from django.test import TestCase
from ..models import Service
from django.contrib.auth.models import User
# Create your tests here.


class SericeModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('admin', 'hello@gmail.com','20072604sh')
        Service.objects.create(title='name', description = 'second', service_user = user)
        
    def test_title_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название услуги')
        
    def test_description_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'Описание услуги')
        
    def test_service_user_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('service_user').verbose_name
        self.assertEquals(field_label, 'Продавец')
        
    def test_title_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
        
    # def test_service_user_related_name(self):
    #     service = Service.objects.get(id =1)
    #     related_name  = service._meta.get_field('service_user').related_model
    #     self.assertEquals(related_name, 'user_service')
    
    def test_object_name_is_title(self):
        service = Service.objects.get(id =1)
        expected_object_name = service.title
        self.assertEquals(expected_object_name, str(service))
        
        
        
    
