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
from django.urls import path
from boiAPI.views import arrobas,arroba_por_estado,inserir,inserir_url,home
from boiAPI.views import delete, update,arroba_por_animal,date_boi,render_custom_api
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('arroba',arrobas), #GET
#    path('arroba/<str:date>/',date_boi,name='arrobas do dia'),# get por data
    path('update',inserir), # POST
    path('page/',render_custom_api,name='html customizado'), #GET
    path('',home,name='bem vindo a BOIAPI'),# GET para a home do site
    path('arroba/<str:estado>',arroba_por_estado,name='arroba por estado'), # GET
    path('arroba/<str:animal>',arroba_por_animal,name='animais por estado'),# GET
#    path('update/<str:date>/<str:animal>/<int:arroba>/<str:estado>/<str:regiao>',inserir_url,name='arroba_por_estado'), # POST
    path('delete/<int:id>',delete,name='delete'), # DELETE
]
