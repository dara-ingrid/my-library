from django.shortcuts import render, get_object_or_404

from library.models import Livraria

def index(request):
    livros = Livraria.objects.order_by("data_publicacao").filter(disponivel=True)
    return render(request, 'library/index.html', {"cards": livros})

def imagem(request, foto_id):
    livro = get_object_or_404(Livraria, pk=foto_id)
    return render(request, 'library/imagem.html', {"livro": livro})

def buscar(request):
    livros = Livraria.objects.order_by("data_publicacao").filter(disponivel=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            livros = livros.filter(titulo__icontains=nome_a_buscar)

    return render(request, "library/buscar.html", {"cards": livros})