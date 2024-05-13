from django import forms
from estoque.models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta():
        model = Produto
        fields = '__all__'


    def clean_valor(self):
        valor = self.cleaned_data.get('valor')

        if valor <= 0:
            raise forms.ValidationError('O valor deve ser maior que 0.')
        else:
            return valor