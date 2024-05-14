from django.db import models


class UnidadeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    unidade = models.CharField(max_length=30)

    def __str__(self):
        return self.unidade

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, related_name='medida_produto')
    quantidade = models.IntegerField()
    valor = models.FloatField()
    data_entrada = models.DateField(auto_now_add=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipo_produto')


    def __str__(self):
        return self.nome
    

class ProdutoInventario(models.Model):
    tot_produtos = models.IntegerField()
    tot_valor = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_registro']

    def __str__(self):
        return f'{self.tot_quantidade} - {self.tot_valor}'
    
