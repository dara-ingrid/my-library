from django.shortcuts import render, get_object_or_404, redirect

from apps.library.models import Livraria

from apps.library.forms import LivrariaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    livros = Livraria.objects.order_by("data_publicacao").filter(disponivel=True)
    return render(request, 'library/index.html', {"cards": livros})

def imagem(request, foto_id):
    livro = get_object_or_404(Livraria, pk=foto_id)
    return render(request, 'library/imagem.html', {"livro": livro})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    livros = Livraria.objects.order_by("data_publicacao").filter(disponivel=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            livros = livros.filter(titulo__icontains=nome_a_buscar)

    return render(request, "library/buscar.html", {"cards": livros})


def nova_imagem(request):

    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')

    form = LivrariaForms
    if request.method == 'POST':
        form = LivrariaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo livro cadastrado')
            return redirect('index')

    return render(request, 'library/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass