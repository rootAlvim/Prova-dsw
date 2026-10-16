from django.shortcuts import render
from django.http import HttpResponse
from .models import Equipe, Modalidade
def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, 'index.html', {'equipes': equipes, 'modalidades': modalidades})

def equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    
    return render(request, 'equipe.html', {'equipe': equipe})

def modalidade(request, id):
    modalidade = Modalidade.objects.get(id=id)
    return render(request, 'modalidade.html', {'modalidade': modalidade})

