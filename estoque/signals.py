from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from estoque.models import Produto, ProdutoInventario

def produto_update_inventario():
    tot_produtos = Produto.objects.all().count()
    ProdutoInventario.objects.create(
        tot_produtos= tot_produtos
    )

@receiver(post_save, sender=Produto)
def produto_post_save(sender, instance, created, **kwargs):
    if created:
        produto_update_inventario()


@receiver(post_delete, sender=Produto)
def produto_post_delete(sender, instance, **kwargs):
    produto_update_inventario()