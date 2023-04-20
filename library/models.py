from django.db import models

class Livraria(models.Model):
    titulo = models.TextField(max_length=100, null=False, blank=False)
    autor = models.CharField(max_length=100, null=False, blank=False)
    capa_livro = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Livro [titulo={self.titulo}]"
