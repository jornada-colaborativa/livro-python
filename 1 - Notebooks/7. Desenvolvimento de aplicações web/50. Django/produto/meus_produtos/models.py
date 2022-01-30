from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=150)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    def __str__(self):
        return f'Produto: {self.nome} / Preço: R$ {self.preco}'