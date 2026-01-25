from django.db import models
import datetime 

# Create your models here.
class Boi (models.Model):
    date = models.CharField(max_length=10)
    animal = models.CharField(max_length=20,blank=False)
    arroba = models.FloatField()
    estado = models.CharField(max_length=2)
    regiao = models.CharField(max_length=20)

class Estado (models.Model):
    estado = models.CharField(max_length=25,default='SP')
    regiao = models.CharField(max_length=20,default='oeste')

    def __str__(self):
        return f"{self.estado},{self.regiao}"

class Animal (models.Model):
    data = models.DateField(default='2026-01-01')
    nome = models.CharField(max_length=20,default='boi gordo')
    # a idade e medida em meses 
    idade = models.IntegerField(default=36)
    arroba = models.FloatField(default=300)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='animais')

    def __str__(self):
        return f"{self.nome},{self.data},{self.idade},{self.arroba}"
