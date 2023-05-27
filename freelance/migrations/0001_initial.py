# Generated by Django 4.2 on 2023-05-15 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('slug', models.SlugField(verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание услуги')),
                ('catergory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='freelance.category', verbose_name='категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_service', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название заказа')),
                ('description', models.TextField(verbose_name='Описание заказа')),
                ('catergory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='freelance.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_order', to=settings.AUTH_USER_MODEL, verbose_name='Заказшик')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service/image/')),
                ('obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_media', to='freelance.service')),
            ],
        ),
    ]