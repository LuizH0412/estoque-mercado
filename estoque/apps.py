from django.apps import AppConfig


class EstoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estoque'

    # Função que faça com que o Django "saiba" que tem signals no sistema
    def ready(self):
        import estoque.signals