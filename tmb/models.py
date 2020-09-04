from django.db import models


class TMB(models.Model):
    altura = models.IntegerField()
    peso = models.IntegerField()

    MY_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),

    )

    sexo = models.CharField(max_length=1, choices=MY_CHOICES)

    def __str__(self):
        return self.altura

