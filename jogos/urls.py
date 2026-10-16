from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('',index,name='index'),
    path('equipes/<int:id>/',equipe,name='equipe'),
    path('modalidade/<int:id>/',modalidade,name='modalidade'),
]
