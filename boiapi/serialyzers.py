from rest_framework import serializers
from boiAPI.models import Boi

class Boiserialyzer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.CharField()
    animal = serializers.CharField()
    arroba = serializers.FloatField()
    estado = serializers.CharField()
    regiao = serializers.CharField()

    def create(self, validated_data): # necessario para usar serialyzer.save nas views.py(instancia)
        """
        Cria e retorna uma nova instância de 'Boi', dado os dados validados.
        """
        return Boi.objects.create(**validated_data)
    
    def update (self,instance,validated_data):
        """
        Atualiza e retorna uma instância de `Boi` existente, 
        dado os dados validados.
        """
        # A instância (o boi específico que estamos atualizando) 
        # já está disponível como 'instance'.
        # Atualiza o(s) campo(s) com os novos valores de 'validated_data'
        instance.arroba = validated_data.get(instance.arroba)
        instance.save()
        return instance 
