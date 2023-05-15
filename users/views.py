from django.shortcuts import redirect, render

from users.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        user = auth.authenticate(
            request,
            username=nome,
            password=senha
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request,f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login!')
            return redirect('login')



    return render(request, "users/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome = form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existe!')
                return redirect('cadastro')

            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            user.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')

    return render(request, "users/cadastro.html", {"form": form})

def logout(request):
    messages.success(request, 'Logout efetuado com sucesso!')
    auth.logout(request)
    return redirect('login')