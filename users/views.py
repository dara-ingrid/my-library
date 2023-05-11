from django.shortcuts import render

from users.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, "users/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, "users/cadastro.html", {"form": form})