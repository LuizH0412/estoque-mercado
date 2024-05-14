from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from estoque.models import Produto, ProdutoInventario

@receiver(post_save, sender=Produto)
def produto_post_save(sender, instance, **kwargs):
    tot_produtos = Produto.objects.all().count()
    tot_valor = Produto.objects.aggregate(
        total_valor=Sum('valor')
    )['total_valor']
    ProdutoInventario.objects.create(
        tot_produtos= tot_produtos,
        tot_valor= tot_valor,
    )


@receiver(post_delete, sender=Produto)
def produto_post_delete(sender, instance, **kwargs):