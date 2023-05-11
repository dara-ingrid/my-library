from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: Maria Clara"                
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: Maria Clara"                
            }
        )
    )
    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Ex: mariaclara@xpto.com"                
            }
        )
    )
    senha_1=forms.EmailField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Insira sua senha"                
            }
        )
    )
    senha_2=forms.EmailField(
        label="Confirme sua senha",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder" : "Insira sua senha novamente"                
            }
        )
    )