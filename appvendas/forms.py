from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['valor', 'forma_pagamento', 'nome_procedimento']
