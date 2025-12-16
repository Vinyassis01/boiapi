from django.db import models
import datetime 

# Create your models here.
class Boi (models.Model):
    date = models.CharField(max_length=10)
    animal = models.CharField(max_length=20,blank=False)
    arroba = models.FloatField()
    estado = models.CharField(max_length=2)
    regiao = models.CharField(max_length=20)
