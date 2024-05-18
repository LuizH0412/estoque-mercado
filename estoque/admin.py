from django.contrib import admin
from estoque.models import Produto, Tipo, UnidadeMedida, Feedback, Profissao

# Classe que permite que na tela de admin o usúario possa visualizar e pesquisar os itens
class TipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')

# Classe que permite que na tela de admin o usúario possa visualizar e pesquisar os itens
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'medida', 'quantidade', 'valor_unidade', 'data_entrada', 'categoria')
    search_fields = ('id', 'nome', 'data_entrada')

# Classe que permite que na tela de admin o usúario possa visualizar e pesquisar os itens
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidade')
    search_fields = ('unidade',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'profissao', 'assunto')
    search_fields = ('id', 'nome', 'profissao', 'assunto')

class ProfissaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('id', 'nome')



admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(UnidadeMedida, MedidaAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Profissao, ProfissaoAdmin)

