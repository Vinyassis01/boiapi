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
from boiAPI.views import Filtrar_Boi_Gordo_Valor_Data, Animal_reposicaoPageViewSet, Boi_gordoPageViewSet
from boiAPI.views import Filtrar_Animal_reposicao_Valor_Data, Animal_reposicaoViewSet, Boi_gordoViewSet
from boiAPI.views import Filtrar_Boi_Gordo_Data

#filtros
filtrar_boi_gordo = Filtrar_Boi_Gordo_Valor_Data.as_view({'get':'list'})
filtrar_animais_reposicao = Filtrar_Animal_reposicao_Valor_Data.as_view({'get':'list'})
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
    path('reposicao/valor/',filtrar_animais_reposicao, name='filtrar por estado, animal, data e ou limiar(valor animal)'),
    # filtros boi
    path('boigordo/valor/',filtrar_boi_gordo, name='filtrar boi gordo por estado, data e ou arroba a vista(limiar)'),   
]
