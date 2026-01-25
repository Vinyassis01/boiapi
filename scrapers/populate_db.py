import os
import django
import datetime

# 1. Aponta para o arquivo settings.py do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boiapi.settings')

# 2. Carrega as configurações do Django
django.setup()

# 3. SÓ AGORA você pode importar os models
from boiAPI.models import Estado, Animal

# Seu código de criação aqui...
def popular():
    data = datetime.date.today()
    estado_mg = Estado.objects.create(nome='Minas Gerais',regiao='leste')
    
    animais = [
        Animal(nome="boi",date=data,idade=30,arroba=300.15, estado=estado_mg),
        Animal(nome="vaca",date=data,idade=42,arroba=267.15, estado=estado_mg),
        Animal(nome="novilha",date=data,idade=18,arroba=330.15, estado=estado_mg),
    ]
    
    # bulk_create economiza consultas ao banco (performance)
    Animal.objects.bulk_create(animais)
    print("Banco povoado com sucesso!")

