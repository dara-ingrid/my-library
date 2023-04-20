from django.contrib import admin

from library.models import Livraria

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor")
    list_display_links = ("id", "titulo")
    search_fields = ("titulo"),

admin.site.register(Livraria, ListandoLivros)