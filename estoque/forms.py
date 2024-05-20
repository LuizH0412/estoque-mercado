from django import forms
from estoque.models import Produto, Feedback


# Classe Form que é utilizada para o cadastro de novos produtos e filtra eles pelo valor e quantidade
class ProdutoModelForm(forms.ModelForm):
    class Meta():
        model = Produto
        fields = '__all__'

    def clean_valor_unidade(self):
        valor = self.cleaned_data.get('valor_unidade')
        if valor <= 0:
            raise forms.ValidationError('O valor deve ser maior que 0.')
        else:
            return valor
        
    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError('Não é possivel cadastrar 0 ou menos itens.')
        else:
            return quantidade

# Classe Form que é utilizada para o cadastro de feedbacks de visitantes do site.
class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields = '__all__'
    

    def clean_texto(self):
        texto = self.cleaned_data.get('texto')
        if len(texto) < 10:
            raise forms.ValidationError('O texto do feedback deve ter no mínimo 10 caracteres.')
        else:
            return texto
        


