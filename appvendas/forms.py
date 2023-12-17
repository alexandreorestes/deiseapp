from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['valor', 'nome_cliente', 'nome_procedimento', 'forma_pagamento']



 
