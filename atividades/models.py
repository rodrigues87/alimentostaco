from django.db import models


class Atividade(models.Model):

    nome = models.CharField(max_length=40)
    corretor = models.DecimalField(max_digits=4, decimal_places=3)

    def __str__(self):
        return self.nome

