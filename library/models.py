from django.db import models

class Livraria(models.Model):

    OPCOES_CATEGORIA = [
        ("AUTOAJUDA", "Autoajuda"),
        ("PROGRAMAÇÃO", "Programação"),
        ("CULINÁRIA", "Culinária"),
        ("FICÇÃO CIENTÍFICA", "Ficção Científica"),
    ]

    titulo = models.TextField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    capa_livro = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Livro [titulo={self.titulo}]"
