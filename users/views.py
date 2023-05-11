from django.shortcuts import redirect, render

from users.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    return render(request, "users/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():

            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro')

            nome = form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            user.save()
            return redirect('login')

    return render(request, "users/cadastro.html", {"form": form})