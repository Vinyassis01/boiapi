from django.shortcuts import render
from django.db.models import IntegerField, Value
from django.db.models.functions import Cast, Replace, Left
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from boiAPI.models import Animal, Estado, Animal_reposicao, Boi_gordo
from boiapi.serialyzers import AnimalSerialyzer,EstadoSerialyzer,Animal_reposicao_Serializer,Boi_gordo_Serializer
# Create your views here.

# views para modificar (read, update, delete)
class Boi_gordoViewSet(viewsets.ModelViewSet):
#    template_name = ''
#    permission_classes = [permissions.IsAuthenticated] 
    queryset = Boi_gordo.objects.all()[:100]
    serializer_class = Boi_gordo_Serializer

    def get_queryset(self):
        return Boi_gordo.objects.all()
    
class Animal_reposicaoViewSet(viewsets.ModelViewSet):
#    template_name = ''    
#    permission_classes = [permissions.IsAuthenticated] 
    queryset= Animal_reposicao.objects.all()[:100]
    serializer_class = Animal_reposicao_Serializer

    def get_queryset(self):
        return Animal_reposicao.objects.all()

# views apenas para leitura
class Boi_gordoPageViewSet(viewsets.ReadOnlyModelViewSet):
#    template_name = ''    
    queryset = Boi_gordo.objects.all()[:100]
    serializer_class = Boi_gordo_Serializer

class Animal_reposicaoPageViewSet(viewsets.ReadOnlyModelViewSet):
#    template_name = ''
    queryset = Animal_reposicao.objects.all()[:100]
    serializer_class = Animal_reposicao_Serializer

class Animal_reposicaoPageViewSet_Estado(viewsets.ReadOnlyModelViewSet):
    serializer_class = Animal_reposicao_Serializer
    def get_queryset(self): 
        # Pegamos o valor do parâmetro 'estado' da URL
        estado = self.kwargs.get('estado')
        queryset = Animal_reposicao.objects.filter(estado__iexact=estado)[:100]
        return queryset

class Filtrar_Boi_Gordo_Valor(viewsets.ReadOnlyModelViewSet):
    serializer_class= Boi_gordo_Serializer
    def get_queryset(self):
        # Pegamos o valor do parâmetro 'estado' e 'limiar' da URL se disponiveis
        estado = self.kwargs.get('estado')
        limiar = self.kwargs.get('limiar')
        if estado :
            queryset =  Boi_gordo.objects.filter(estado__iexact=estado)

        if limiar:
            queryset = Boi_gordo.objects.all()
            queryset = queryset.annotate(
                valor_inteiro=Cast(
                    Left(Replace('arroba_a_vista', Value(','), Value('.')), 4),
                    output_field=IntegerField()
                )
            ).filter(valor_inteiro__gt=int(limiar))

        return queryset

class Filtrar_Animal_reposicao_Valor(viewsets.ReadOnlyModelViewSet):
    serializer_class = Animal_reposicao_Serializer
    def get_queryset(self):
        limiar = self.kwargs.get('limiar')
        animal = self.kwargs.get('animal')
        estado = self.kwargs.get('estado')

        if animal and not estado:
            queryset =  Animal_reposicao.objects.filter(animal__iexact=animal)

        if estado and not animal:
            queryset = Animal_reposicao.objects.filter(estado__iexact=estado)

        if animal and estado:
            queryset = Animal_reposicao.objects.filter(estado__iexact=estado,animal__iexact=animal)

        if limiar:
            queryset = queryset.annotate(
                valor_inteiro=Cast(
                    Left(Replace('valor_animal', Value(','), Value('.')), 4),
                    output_field=IntegerField()
                )
            ).filter(valor_inteiro__gt=int(limiar))

        return queryset
        


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return Response({'status': 'online'})

