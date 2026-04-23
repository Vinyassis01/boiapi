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

class Filtrar_Boi_Gordo_Valor_Data(viewsets.ReadOnlyModelViewSet):
    serializer_class= Boi_gordo_Serializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'request_boi_gordo.html'
    def get_queryset(self):
        # Pegamos o valor do parâmetro 'estado' e 'limiar' da URL se disponiveis
        estado = self.request.query_params.get('estado')
        limiar = self.request.query_params.get('limiar')
        data = self.request.query_params.get('data')
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')

        queryset = Boi_gordo.objects.all()

        if data:
            queryset = queryset.filter(data=data) # "="

        if data_inicio and data_fim:
            queryset = queryset.filter(data__range=(data_inicio,data_fim))

        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio) # ">="

        if data_fim:
            queryset = queryset.filter(data__lte=data_fim) # "<="

        if estado :
            queryset = queryset.filter(estado__iexact=estado)

        if estado and data:
            queryset = queryset.filter(data=data, estado__iexact=estado)

        if limiar:
            queryset = queryset.annotate(
                valor_inteiro=Cast(
                    Left(Replace('arroba_a_vista', Value(','), Value('.')), 4),
                    output_field=IntegerField()
                )
            ).filter(valor_inteiro__gt=int(limiar))

        return queryset

    def list(self, request, *args, **kwargs):
        # 1. Obtém o queryset filtrado
        queryset = self.get_queryset()
        
        # 2. Serializa os dados (opcional, mas recomendado para formatar campos)
        serializer = self.get_serializer(queryset, many=True)
        
        # 3. Retorna os dados dentro da chave 'data' para o template
        return Response({'data': serializer.data})
          

class Filtrar_Animal_reposicao_Valor_Data(viewsets.ReadOnlyModelViewSet):
    serializer_class = Animal_reposicao_Serializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'request_reposicao.html'
    def get_queryset(self):
        limiar = self.request.query_params.get('limiar')
        animal = self.request.query_params.get('animal')
        estado = self.request.query_params.get('estado')        
        data = self.request.query_params.get('data')
        data_inicio = self.request.query_params.get('data_inicio')
        data_fim = self.request.query_params.get('data_fim')

        queryset = Animal_reposicao.objects.all()

        if animal and estado:
            queryset = queryset.filter(estado__iexact=estado,animal__iexact=animal)

        if animal:
            queryset = queryset.filter(animal=animal)

        if estado:
            queryset = queryset.filter(estado__iexact=estado)

        if limiar:
            queryset = queryset.annotate(
                valor_inteiro=Cast(
                    Left(Replace('valor_animal', Value(','), Value('.')), 4),
                    output_field=IntegerField()
                )
            ).filter(valor_inteiro__gt=int(limiar))

        if data:
            queryset = queryset.filter(data=data) # "="

        if data_inicio and data_fim:
            queryset = queryset.filter(data__range=(data_inicio,data_fim))

        if data_inicio:
            queryset = queryset.filter(data__gte=data_inicio) # ">="

        if data_fim:
            queryset = queryset.filter(data__lte=data_fim)

        return queryset

    def list(self, request, *args, **kwargs):
        # 1. Obtém o queryset filtrado
        queryset = self.get_queryset()
        
        # 2. Serializa os dados (opcional, mas recomendado para formatar campos)
        serializer = self.get_serializer(queryset, many=True)
        
        # 3. Retorna os dados dentro da chave 'data' para o template
        return Response({'data': serializer.data})
     
class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return Response({'status': 'online'})

