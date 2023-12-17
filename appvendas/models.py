from django.db import models

class Venda(models.Model):
    FORMAS_DE_PAGAMENTO = [
        ('pix', 'Pix'),
        ('debito', 'Débito'),
        ('credito_vista', 'Crédito'),
        ('dinheiro', 'Dinheiro'),
        ('troca', 'Troca'),
        ('fiado', 'Fiado'),
    ]
    PROCEDIMENTOS = [
        ('corte', 'Corte'),
        ('escova', 'Escova'),
        ('luzes', 'Luzes'),
        ('mecha', 'Mecha'),
        ('tratamento', 'Selagem'),
        ('ozonio', 'Ozônio'),
        ('plastica', 'Plástica'),
        ('coloracao', 'Coloração'),
    ]

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20, choices=FORMAS_DE_PAGAMENTO)
    data = models.DateField(auto_now_add=True)
    nome_procedimento =  models.CharField(max_length=30, choices=PROCEDIMENTOS)
    nome_cliente = models.CharField(max_length=100, default=' ')

    def __str__(self):
        return f"{self.nome_procedimento} - R$ {self.valor} ({self.data})"

