"""
URL configuration for boiapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include 
# views somente para leitura
from boiAPI.views import Boi_gordoPageViewSet, Animal_reposicaoPageViewSet, HomeView
# views para modificar (read, update, delete)
from boiAPI.views import Boi_gordoViewSet, Animal_reposicaoViewSet
# views para filtros (animal, estado ,valor animal, data)
from boiAPI.views import Filtrar_Boi_Gordo_Valor, Animal_reposicaoPageViewSet, Boi_gordoPageViewSet
from boiAPI.views import Filtrar_Animal_reposicao_Valor, Animal_reposicaoViewSet, Boi_gordoViewSet
from boiAPI.views import Filtrar_Boi_Gordo_Data

#filtros
filtrar_boi_gordo = Filtrar_Boi_Gordo_Valor.as_view({'get':'list'})
filtrar_animais_reposicao = Filtrar_Animal_reposicao_Valor.as_view({'get':'list'})
filtrar_boi_gordo_data = Filtrar_Boi_Gordo_Data.as_view({'get':'list'})

# modificacoes
modificar_animal_reposicao = Animal_reposicaoViewSet.as_view({'post': 'create','put':'update','patch':'partial_update','delete':'destroy'})
modificar_boi_gordo = Boi_gordoViewSet.as_view({'post': 'create','put':'update','patch':'partial_update','delete':'destroy'})

# listagem
listar_animais_reposicao = Animal_reposicaoPageViewSet.as_view({'get':'list'})
listar_boi_gordo = Boi_gordoPageViewSet.as_view({'get':'list'}) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    # model Boi_gordo
    path('boi_gordo/<int:pk>/modificar/', modificar_boi_gordo, name= 'modificar boi gordo'),
    path('boi_gordo/<int:pk>/delete/', modificar_boi_gordo, name= 'deletar boi_gordo'),
    path('boi_gordo/inserir/', modificar_boi_gordo, name='inserir boi gordo'),
    path('boi_gordo/', listar_boi_gordo, name='listar valores do boi'),
    # model Animais_reposicao
    path('animais_reposicao/<int:pk>/modificar/', modificar_animal_reposicao, name= 'modificar animal de reposicao'),
    path('animais_reposicao/<int:pk>/delete/', modificar_animal_reposicao, name='deletar animal de reposicao'),
    path('reposicao/inserir/', modificar_animal_reposicao, name='inserir animal reposicao'),
    path('animal_reposicao/', listar_animais_reposicao, name='listar valores de animais para reposicao'),
    # filtros reposicao
    path('reposicao/estado/<str:estado>',filtrar_animais_reposicao, name='filtrar por estado'),
    path('reposicao/animal/<str:animal>',filtrar_animais_reposicao, name='filtrar por animal'),
    path('reposicao/estado/<str:estado>/animal/<str:animal>',filtrar_animais_reposicao, name='filtrar por estado e animal'),
    path('reposicao/estado/<str:estado>/limiar/<int:limiar>',filtrar_animais_reposicao,name='filtrar por estado e limiar'),
    path('reposicao/animal/<str:animal>/limiar/<int:limiar>',filtrar_animais_reposicao,name='filtrar por animal e limiar'),
    path('reposicao/estado/<str:estado>/animal/<str:animal>/limiar/<int:limiar>',filtrar_animais_reposicao,name='filtrar por estado, animal e limiar'),
    # filtros boi
    path('boigordo/estado/<str:estado>',filtrar_boi_gordo, name='filtrar boi gordo por estado'),
    path('boigordo/limiar/<int:limiar>',filtrar_boi_gordo, name='filtrar boi gordo por limiar'),
    path('boigordo/estado/<str:estado>/limiar/<int:limiar>',filtrar_boi_gordo, name='filtrar boi gordo por estado e limiar'),
    path('boigordo/data/<str:data>',filtrar_boi_gordo_data),
    path('boigordo/data_inicio/<str:data_inicio>',filtrar_boi_gordo_data),
    path('boigordo/data_fim/<str:data_fim>',filtrar_boi_gordo_data),
    path('boigordo/data_inicio/<str:data_inicio>/data_fim/<str:data_fim>',filtrar_boi_gordo_data),
   
]
