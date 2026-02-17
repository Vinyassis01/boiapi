from rest_framework import serializers
from boiAPI.models import Boi_gordo,Animal_reposicao,Estado,Animal

class EstadoSerialyzer (serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id','estado','regiao']

class AnimalSerialyzer (serializers.ModelSerializer):
    estado = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all())
    class Meta:
        model = Animal
        fields =['data','nome','idade','arroba','estado']

class Animal_reposicao_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Animal_reposicao
        fields = ['estado','animal','valor_animal','relacao_troca_1','relacao_troca_2','data']

class Boi_gordo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Boi_gordo
        fields = ['estado','animal','regiao','arroba_a_vista','arroba_a_prazo','variacao','data']
