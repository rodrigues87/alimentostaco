from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from alimentostacoaz.models import Alimento
from usuarios.models import User


class Dieta(models.Model):
    nome = models.CharField(max_length=255)
    alimentos = models.ManyToManyField(Alimento, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observacao = models.TextField(max_length=600, blank=True, null=True)
    __original_alimentos = None

    total_alanine_g = models.FloatField(blank=True, null=True)
    total_arginine_g = models.FloatField(blank=True, null=True)
    total_ashes_g = models.FloatField(blank=True, null=True)
    total_aspartic_g = models.FloatField(blank=True, null=True)
    total_calcium_mg = models.FloatField(blank=True, null=True)
    total_carbohydrate_g = models.FloatField(blank=True, null=True)
    total_cholesterol_mg = models.FloatField(blank=True, null=True)
    total_copper_mg = models.FloatField(blank=True, null=True)
    total_cystine_g = models.FloatField(blank=True, null=True)
    total_energy_kcal = models.FloatField(blank=True, null=True)
    total_energy_kj = models.FloatField(blank=True, null=True)
    total_fiber_g = models.FloatField(blank=True, null=True)
    total_glutamic_g = models.FloatField(blank=True, null=True)
    total_glycine_g = models.FloatField(blank=True, null=True)
    total_histidine_g = models.FloatField(blank=True, null=True)
    total_humidity_percents = models.FloatField(blank=True, null=True)
    total_iron_mg = models.FloatField(blank=True, null=True)
    total_isoleucine_g = models.FloatField(blank=True, null=True)
    total_leucine_g = models.FloatField(blank=True, null=True)
    total_lipidius_g = models.FloatField(blank=True, null=True)
    total_lysine_g = models.FloatField(blank=True, null=True)
    total_magnesium_mg = models.FloatField(blank=True, null=True)
    total_manganese_mg = models.FloatField(blank=True, null=True)
    total_methionine_g = models.FloatField(blank=True, null=True)
    total_monounsaturated_g = models.FloatField(blank=True, null=True)
    total_niacin_mg = models.FloatField(blank=True, null=True)
    total_phenylalanine_g = models.FloatField(blank=True, null=True)
    total_phosphorus_mg = models.FloatField(blank=True, null=True)
    total_polyunsaturated_g = models.FloatField(blank=True, null=True)
    total_potassium_mg = models.FloatField(blank=True, null=True)
    total_proline_g = models.FloatField(blank=True, null=True)
    total_protein_g = models.FloatField(blank=True, null=True)
    total_pyridoxine_mg = models.FloatField(blank=True, null=True)
    total_rae_mcg = models.FloatField(blank=True, null=True)
    total_re_mcg = models.FloatField(blank=True, null=True)
    total_retinol_mcg = models.FloatField(blank=True, null=True)
    total_riboflavin_mg = models.FloatField(blank=True, null=True)
    total_saturated_g = models.FloatField(blank=True, null=True)
    total_serine_g = models.FloatField(blank=True, null=True)
    total_sodium_mg = models.FloatField(blank=True, null=True)
    total_threonine_g = models.FloatField(blank=True, null=True)
    total_tiamina_mg = models.FloatField(blank=True, null=True)
    total_tryptophan_g = models.FloatField(blank=True, null=True)
    total_tyrosine_g = models.FloatField(blank=True, null=True)
    total_valine_g = models.FloatField(blank=True, null=True)
    total_vitaminc_mg = models.FloatField(blank=True, null=True)
    total_zinc_mg = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        alimentos = self.alimentos.all()

        self.total_ashes_g = 0

        for alimento in alimentos:
            self.total_ashes_g = self.total_ashes_g + alimento.ashes_g

        print(alimentos)

        super(Dieta, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'dieta'
