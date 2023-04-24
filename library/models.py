from django.db import models

from datetime import datetime

class Livraria(models.Model):

    OPCOES_CATEGORIA = [
        ("AUTOAJUDA", "Autoajuda"),
        ("PROGRAMAÇÃO", "Programação"),
        ("CULINÁRIA", "Culinária"),
        ("FICÇÃO", "Ficção"),
    ]

    titulo = models.CharField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    capa_livro = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    disponivel = models.BooleanField(default=True)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.titulo
