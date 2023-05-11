from django.shortcuts import render

from users.forms import LoginForms

def login(request):
    form = LoginForms()
    return render(request, "users/login.html", {"form": form})

def cadastro(request):
    return render(request, "users/cadastro.html")