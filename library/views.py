from django.shortcuts import render

def index(request):

    dados = {
    1: {"titulo": "Código limpo: Habilidades práticas do Agile Software",
        "autor": "Robert C. Martin"},
    2: {"titulo": "Mais esperto que o Diabo: O mistério revelado da liberdade e do sucesso",
        "autor": "Napoleon Hill"},
    }
    
    return render(request, 'library/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'library/imagem.html')