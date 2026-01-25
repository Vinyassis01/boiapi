from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from boiAPI.models import Boi,Animal,Estado
from boiapi.serialyzers import Boiserialyzer,AnimalSerialyzer,EstadoSerialyzer
from datetime import datetime
# Create your views here.

class EstadoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Estado.objects.all()
    serializer_class = EstadoSerialyzer

    def get_queryset(self):
        return Estado.objects.all()
    
class AnimalViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset= Animal.objects.all()
    serializer_class = AnimalSerialyzer

class AnimalPageViewSet(viewsets.ReadOnlyViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerialyzer

class EstadoPageViewSet(viewsets.ReadOnlyViewSet):
    queryset = Estado.objects.all()
    serializer_class = AnimalSerialyzer

@api_view(["GET"])
def date_boi(request,date):
    try:
        valores_estado = Boi.objects.filter(date=date) # estado=estado e necessario para os parametros na url
        serializador = Boiserialyzer(valores_estado,many=True)
        return Response(serializador.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"]) # OK
@renderer_classes([TemplateHTMLRenderer])
def arrobas (request):
    try:
        valores = Boi.objects.all()
        serializador = Boiserialyzer(valores,many=True) # many=True e necessario para consultar varios valores
        data = serializador.data
        return Response({"dados":data},template_name='boiAPI/main.html')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"]) # OK
@renderer_classes([TemplateHTMLRenderer])  
def arroba_por_estado (request,estado):
    try:
        valores_estado = Boi.objects.filter(estado=estado) # estado=estado e necessario para os parametros na url
        serializador = Boiserialyzer(valores_estado,many=True)
        data = serializador.data
        return Response({"dados":data},template_name='boiAPI/main.html')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])    
def arroba_por_animal (request,animal):
    try:
        valores_estado = Boi.objects.filter(animal=animal) # animal=animal e necessario para os parametros na url
        serializador = Boiserialyzer(valores_estado,many=True)
        data = serializador.data
        return Response({"dados":data},template_name='boiAPI/main.html')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["POST","GET"])
# curl http://127.0.0.1:8000/update --json '{"date":"2025-12-23","animal":"bezerro desmamado","arroba":"446.15","estado":"SP","regiao":"SP"}'
def inserir(request):
    try:
        if request.method == "POST": # verifica se o metodo e post
            serializador = Boiserialyzer(data=request.data) # serializa os dados da requisicao
            if serializador.is_valid() : # verifica se o serializador e valido
                serializador.save() # salva (prescisa de um metodo create no serialyzers.py)
                return Response(serializador.data,status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST","GET"]) # curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/update/garrote/260/pr/norte
def inserir_url(request,date,animal,arroba,estado,regiao): # mas retorna  400
    try:
        if request.method == "POST": # verifica se o metodo e post
            boi_instance = Boi.objects.create(date=date,animal=animal,arroba=arroba,estado=estado,regiao=regiao)
            serializador = Boiserialyzer(data=boi_instance) # serializa os dados da requisicao
            if serializador.is_valid() : # verifica se o serializador e valido
                serializador.save() # salva (prescisa de um metodo create no serialyzers.py)
            return Response(serializador.data,status=status.HTTP_201_CREATED)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"]) # OK
def delete(request,id): # funciona com curl >> curl -X DELETE http://127.0.0.1:8000/delete/5
    try:
        valores = Boi.objects.get(id=id) # mas retorna 400
        valores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["PATCH","GET"])
def update (request,id):
    try:
        item = Boi.objects.filter(id=id).exists()
        if request.method == "PATCH":
            serializador = Boiserialyzer(request.data,partial=True)
            if serializador.is_valid():
                serializador.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        elif request.method == "GET":
            serializador = Boiserialyzer(data=request.data,partial=True)
            return Response(serializador.data)
    except:
        return Response(status=status.HTTP_304_NOT_MODIFIED)
   
@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def render_custom_api(request):
    # Buscando dados do banco de dados
    dados = Boi.objects.all()
    serializador = Boiserialyzer(dados,many=True)
    data = serializador.data
    # O Response recebe o dicionário de contexto e o template_name
    return Response({"dados":data},template_name='boiAPI/main.html')

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def home(request):
    dados ={"bem vindo":"de uma olhada na API"}
    return Response(dados,template_name='boiAPI/home.html')