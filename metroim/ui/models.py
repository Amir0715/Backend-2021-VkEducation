from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.template.defaultfilters import slugify

class City(models.Model):
    name = models.CharField('Название города', max_length=64)

class Line(models.Model):
    name = models.CharField('Название линии', max_length=64)
    # В будущем создать кастомное поле для работы с hex-числом
    hex_color = models.CharField('Название линии', max_length=6)
    city = ForeignKey('City', verbose_name='Город', on_delete=models.CASCADE, related_name='lines')
    

class Station(models.Model):
    name = models.CharField('Название станции', max_length=64)
    order = models.PositiveSmallIntegerField('Порядок')
    latitude = models.FloatField('Долгота')
    longitude = models.FloatField('Широта')
    line = ForeignKey('Line', verbose_name='Линии', on_delete=models.CASCADE, related_name='stations')
    
