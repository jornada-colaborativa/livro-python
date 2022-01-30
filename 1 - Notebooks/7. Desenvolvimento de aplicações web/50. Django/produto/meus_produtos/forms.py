from django import forms
from .models import Produto

class cadastroForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']
