from django import forms
from apps.library.models import Livraria

class LivrariaForms(forms.ModelForm):
    class Meta:
        model = Livraria
        exclude = ['disponivel',]
        labels = {
            'titulo': 'Título',
            'data_publicacao' :'Data de registro',
            'usuario': 'Usuário'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control',}),
            'autor': forms.TextInput(attrs={'class': 'form-control',}),
            'categoria': forms.Select(attrs={'class': 'form-control',}),
            'capa_livro': forms.FileInput(attrs={'class': 'form-control',}),
            'data_publicacao': forms.DateInput(
                format='%d/%m/%a',
                attrs={
                    'type' : 'date',
                    'class': 'form-control',
                }
            ),
             'usuario': forms.Select(attrs={'class': 'form-control',}),
            
        }