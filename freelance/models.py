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
    category = models.ForeignKey("freelance.Category", verbose_name='Категория', on_delete=models.PROTECT)
    price = models.IntegerField('цена')
    start = models.DateTimeField('Начать',null=True)
    finish = models.DateTimeField('Завершить', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order', verbose_name='Заказшик')
    

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

class Category(models.Model):
    name = models.CharField("Название категории", max_length=50)
    slug = models.SlugField('Url')
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        

class Subcategory(models.Model):
    name = models.CharField("Название подкатегории", max_length=50)
    slug = models.SlugField('Url')
    category = models.ForeignKey((Описаниеn_delete=models.CASCADE, verbose_name='Нкатегория')



    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'

    def __str__(self):
        return f'{self.name}'


class ProfileUser(models):
    profile_img = models.ImageField('фото',upload_to='users/profile/')
    completed_tasks = models.IntegerField('выполненные задачи')
    create_tasks = models.IntegerField('созданные задачи')
    user = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name='Создатель')


    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.user.username}'


class Reviews(models.Model):
    order = models.ForeignKey('freelance.Order',on_delete=models.CASCADE,verbose_name='Задание')
    grade = models.IntegerField('')
    description = models.TextField('Описание')
    created = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'{self.order}'
