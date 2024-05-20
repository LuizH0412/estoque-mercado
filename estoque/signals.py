from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from estoque.models import Produto, ProdutoInventario, Feedback, FeedbackContagem

# Função que cria no banco de dados um novo registro de feedback
def feedback_update_contagem():
    tot_feedback = Feedback.objects.all().count()
    FeedbackContagem.objects.create(
        tot_feedback= tot_feedback
    )

# Função que cria no banco de dados um novo registro de inventário com a totalidade dos produtos
def produto_update_inventario():
    tot_produtos = Produto.objects.all().count()
    ProdutoInventario.objects.create(
        tot_produtos= tot_produtos
    )

@receiver(post_save, sender=Produto)
def produto_post_save(sender, instance, created, **kwargs):
    if created:
        produto_update_inventario() # Função chamada em caso de pre-save


@receiver(post_delete, sender=Produto)
def produto_post_delete(sender, instance, **kwargs):
    produto_update_inventario() # Função chamada em caso de post-delete


@receiver(post_save, sender=Feedback)
def feedback_post_save(sender, instance, **kwargs):
    feedback_update_contagem() # Função chamada em caso de pre-save


@receiver(post_delete, sender=Feedback)
def feedback_post_delete(sender, instance, **kwargs):
    feedback_update_contagem() # Função chamada em caso de post-delete