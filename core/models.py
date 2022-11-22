from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=120)
    dados = models.CharField(max_length=150)
    valor = models.DecimalField(decimal_places=2,max_digits=5)

    def __str__(self):
        return self.nome