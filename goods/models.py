from email.mime import image
from os import name
from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Categories(models.Model):
    name= models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug= models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name= 'Слаг - дописка в URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    name= models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug= models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name= 'Слаг - дописка в URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='щя фотограф сгоняет за фото')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0, max_digits=3, decimal_places=0, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    category = 
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товарiщ'