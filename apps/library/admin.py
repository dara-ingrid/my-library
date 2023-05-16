from django.contrib import admin

from apps.library.models import Livraria

class ListandoLivros(admin.ModelAdmin):
    list_display = ("id", "titulo", "autor","disponivel")
    list_display_links = ("id", "titulo",)
    search_fields = ("titulo", )
    list_filter = ("categoria","usuario", )
    list_editable = ("disponivel",)
    list_per_page = 10

admin.site.register(Livraria, ListandoLivros)