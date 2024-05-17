from django.db import models


# Modelo que registra no banco de dados os cargos existentes no sistema
class Cargo(models.Model):
    id = models.AutoField(primary_key=True) # Primary Key
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome

# Modelo que registra no banco de dados as profissões existentes no sistema
class Profissao(models.Model):
    id = models.AutoField(primary_key=True) # Primary Key
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome

# Model que registra no banco de dados novas unidades de medida
class UnidadeMedida(models.Model):
    id = models.AutoField(primary_key=True)
    unidade = models.CharField(max_length=30)

    def __str__(self):
        return self.unidade

# Model que registra no banco de dados novos tipos de categoria de produtos
class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

# Model que registra no banco de dados novos produtos
class Produto(models.Model):
    id = models.AutoField(primary_key=True) # Primary Key
    nome = models.CharField(max_length=200)
    medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE, related_name='medida_produto') # Chave estrangeira / Unidade de medida
    quantidade = models.IntegerField()
    valor_unidade = models.FloatField()
    data_entrada = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipo_produto') # Chave estrangeira / Categoria do produto


    def __str__(self):
        return self.nome


# Model que registra no banco de dados a quantidade de produtos totais no estabelecimento e a hora em que foi feito um novo registro de produtos
class ProdutoInventario(models.Model):
    tot_produtos = models.IntegerField()
    data_registro = models.DateTimeField(auto_now_add=True) # Auto incrementação de data e hora

    class Meta:
        ordering = ['-data_registro'] # Ordenando pela data e hora do mais atual ao mais antigo

    def __str__(self):
        return f'{self.tot_quantidade} - {self.tot_valor}'
    

# Model que registra no banco de dados o feedback dos visitantes da página
class Feedback(models.Model):
    id = models.AutoField(primary_key=True) # Primary Key
    nome = models.CharField(max_length=60) # Nome do individuo
    profissao = models.ForeignKey(Profissao, on_delete=models.CASCADE, related_name='feedback_profissao') # Profissão do individuo/Chave estrangeira
    assunto = models.CharField(max_length=200) # Área que o usúario escreve o assunto do Feedback
    texto = models.TextField() # Aréa de texto do usúario e seu feedback
    data_feedback = models.DateTimeField(auto_now_add=True) # Incrementa a data automaticamente no momento do registro
    
    def __str__(self):
        return self.assunto


# Model que registra no banco de dados a quantidade feedback que o site recebeu
class FeedbackContagem(models.Model):
    tot_feedback = models.IntegerField()
    data_registro = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-data_registro'] # Ordenando pela data e hora do mais atual ao mais antigo

    def __str__(self):
        return self.tot_feedback


# Model que registra no banco de dados os funcionários
class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True) # Primary Key
    nome_completo = models.CharField(max_length=60)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='cargo_funcionario')
    email = models.CharField(max_length=40)
    data_contratacao = models.DateField()

    def __str__(self):
        return self.nome

    
