from django.shortcuts import render

def index(request):
    return render(request, 'library/index.html')

def imagem(request):
    return render(request, 'library/imagem.html')