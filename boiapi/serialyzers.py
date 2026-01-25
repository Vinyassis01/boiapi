from rest_framework import serializers
from boiAPI.models import Boi,Animal,Estado

class Boiserialyzer (serializers.Serializer):
    class Meta:
        model = Boi
        fields = ['id','date','animal','arroba','estado','regiao']

class EstadoSerialyzer (serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id','estado','regiao']

class AnimalSerialyzer (serializers.ModelSerializer):
    estado = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all())

    class Meta:
        model = Animal
        fields =['data','nome','idade','arroba','estado']
