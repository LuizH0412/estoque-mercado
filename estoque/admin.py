from django.contrib import admin
from estoque.models import Produto, Tipo


class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data_entrada', 'tipo')
    search_fields = ('id', 'nome', 'data_entrada')



admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tipo, TipoAdmin)

