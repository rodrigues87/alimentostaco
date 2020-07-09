from django.db import models
from alimentostacoaz.models import Alimento
from usuarios.models import User


class Dieta(models.Model):
    nome = models.CharField(max_length=255)
    alimentos = models.ManyToManyField(Alimento, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observacao = models.TextField(max_length=600,blank=True,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'dieta'


