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
from boiAPI.views import arrobas,arroba_por_estado,inserir,inserir_url,home
# views somente para leitura
from boiAPI.views import AnimalPageViewSet, EstadoPageViewSet, Boi_gordoPageViewSet, Animal_reposicaoPageViewSet
# views para modificar (read, update, delete)
from boiAPI.views import Boi_gordoViewSet, Animal_reposicaoViewSet, EstadoViewSet, AnimalViewSet

modificar_animal = AnimalViewSet.as_view({'put':'update','patch':'partial_update','delete':'destroy'})
modificar_estado = EstadoViewSet.as_view({'put':'update','patch':'partial_update','delete':'destroy'})
modificar_animal_reposicao = Animal_reposicaoViewSet.as_view({'put':'update','patch':'partial_update','delete':'destroy'})
modificar_boi_gordo = Boi_gordoViewSet.as_view({'put':'update','patch':'partial_update','delete':'destroy'})
listar_animais = AnimalPageViewSet.as_view({'get':'list'})
listar_estados = EstadoPageViewSet.as_view({'get':'list'})
listar_animais_reposicao = Animal_reposicaoPageViewSet.as_view({'get':'list'})
listar_boi_gordo = Boi_gordoPageViewSet.as_view({'get':'list'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animais/<int:pk>/modificar/', modificar_animal, name= 'modificar animal'),
    path('animais/<int:pk>/delete/', modificar_animal, name='deletar animal'),
    path('estados/<int:pk>/modificar/', modificar_estado, name='modificar estado'),
    path('estados/<int:pk>/delete/', modificar_estado, name='deletar estado'),
    path('animais',listar_animais, name='listar_animais'),
    path('estados',listar_estados, name='listar_estados'),

#    path('api/', include(router.urls)),
#    path('arroba',arrobas), #GET
#    path('arroba/<str:date>/',date_boi,name='arrobas do dia'),# get por data
#    path('update',inserir), # POST
#    path('page/',render_custom_api,name='html customizado'), #GET
#    path('',home,name='bem vindo a BOIAPI'),# GET para a home do site
#    path('arroba/<str:estado>',arroba_por_estado,name='arroba por estado'), # GET
#    path('arroba/<str:animal>',arroba_por_animal,name='animais por estado'),# GET
#    path('update/<str:date>/<str:animal>/<int:arroba>/<str:estado>/<str:regiao>',inserir_url,name='arroba_por_estado'), # POST
#    path('delete/<int:id>',delete,name='delete'), # DELETE
]
