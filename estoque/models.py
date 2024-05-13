from django.db import models


class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
    data_entrada = models.DateField(auto_now_add=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipo_produto')


    def __str__(self):
        return self.nome
    
