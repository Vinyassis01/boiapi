from django.db import models
import datetime 

# Create your models here.
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

class Boi_gordo (models.Model):
    estado = models.CharField(max_length=50,default='')
    animal = models.CharField(max_length=50,default='boi gordo')
    regiao = models.CharField(max_length=50,default='',blank=True)
    arroba_a_vista = models.CharField(max_length=10)
    arroba_a_prazo = models.CharField(max_length=10)
    variacao = models.CharField(max_length=10,default='0,0')
    data = models.DateField()

    def __str__(self):
        return f"{self.estado},{self.animal},{self.regiao},{self.arroba_a_vista},{self.arroba_a_prazo},{self.variacao},{self.data}"


# model para animais de reposicao (machos e femeas nelorados)
# tambem sera usado para animais mesticos
class Animal_reposicao(models.Model):
    estado = models.CharField(max_length=50,default='')
    animal = models.CharField(max_length=50,default='boi gordo')
    valor_animal = models.CharField(max_length=50,default='')
    valor_kg = models.CharField(max_length=10)
    relacao_troca = models.CharField(max_length=10)
    data = models.DateField()

    def __str__(self):
        return f"{self.estado},{self.animal},{self.valor_animal},{self.relacao_troca_1},{self.relacao_troca_2},{self.data}"
