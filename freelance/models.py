from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField('Название услуги', max_length=100)
    description = models.TextField('Описание услуги')
    catergory = models.ForeignKey("freelance.Category", verbose_name='категория', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_service', verbose_name='Продавец')
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'


class Order(models.Model):
    title = models.CharField("Название заказа", max_length=50)
    description = models.TextField('Описание заказа')
    catergory = models.ForeignKey("freelance.Category", verbose_name='Категория', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', verbose_name='Заказшик')
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class Media(models.Model):
    obj = models.ForeignKey("freelance.Service", on_delete=models.CASCADE, related_name='service_media')
    image = models.ImageField(upload_to='service/image/')

    def __str__(self):
        return f'{self.obj}'
    

class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)
    slug = models.SlugField('Url')
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        
        
    