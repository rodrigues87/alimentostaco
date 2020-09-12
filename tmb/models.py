from django.db import models

from atividades.models import Atividade


class TMB(models.Model):
    MY_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Feminino'),

    )

    sexo = models.CharField(max_length=1, choices=MY_CHOICES)

    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    idade = models.IntegerField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    total = models.IntegerField()
    imc = models.IntegerField()
    classificacao = models.CharField(max_length=100)

    def __str__(self):
        return self.altura

    def save(self, *args, **kwargs):
        if self.sexo == "Masculino":
            self.total = 10 * int(self.peso) + 6.25 * int(self.altura) - 5 * int(self.idade) + 5
        if self.sexo == "Feminino":
            self.total = 10 * self.peso + 6.25 * self.altura - 5 * self.idade - 161

        self.total = float(self.total) * float(self.atividade.corretor)

        self.imc = int(self.peso / ((self.altura/100) ** 2))

        if self.idade < 65:
            if self.imc <= 18:
                self.classificacao = "Abaixo do peso"
            if 18 < self.imc < 25:
                self.classificacao = "Peso normal"
            if 25 <= self.imc < 30:
                self.classificacao = "Excesso de peso"
            if 30 <= self.imc < 35:
                self.classificacao = "Obesidade grau I"
            if 35 <= self.imc < 40:
                self.classificacao = "Obesidade grau II (severa)"
            if self.imc >= 40:
                self.classificacao = "Obesidade grau III (mórbida)"
        if self.idade >= 65:
            if self.imc <= 22:
                self.classificacao = "Baixo peso"
            if 22 < self.imc < 27:
                self.classificacao = "Adequado ou eutrófico"
            if self.imc >= 27:
                self.classificacao = "Sobrepeso"

        super(TMB, self).save(*args, **kwargs)
