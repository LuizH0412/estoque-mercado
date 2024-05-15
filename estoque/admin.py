from django.contrib import admin
from estoque.models import Produto, Tipo, UnidadeMedida


class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'medida', 'quantidade', 'valor_unidade', 'data_entrada', 'tipo')
    search_fields = ('id', 'nome', 'data_entrada')

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidade')
    search_fields = ('unidade',)


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(UnidadeMedida, MedidaAdmin)

