from django.shortcuts import render

from library.models import Livraria

def index(request):
    livros = Livraria.objects.all()
    return render(request, 'library/index.html', {"cards": livros})

def imagem(request):
    return render(request, 'library/imagem.html')