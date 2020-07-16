from django.db import models


class Alimento(models.Model):
    alanine_g = models.FloatField(blank=True, null=True)
    arginine_g = models.FloatField(blank=True, null=True)
    ashes_g = models.FloatField(blank=True, null=True)
    aspartic_g = models.FloatField(blank=True, null=True)
    calcium_mg = models.FloatField(blank=True, null=True)
    carbohydrate_g = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_mg = models.FloatField(blank=True, null=True)
    copper_mg = models.FloatField(blank=True, null=True)
    cystine_g = models.FloatField(blank=True, null=True)
    energy_kcal = models.FloatField(blank=True, null=True)
    energy_kj = models.FloatField(blank=True, null=True)
    fiber_g = models.FloatField(blank=True, null=True)
    glutamic_g = models.FloatField(blank=True, null=True)
    glycine_g = models.FloatField(blank=True, null=True)
    histidine_g = models.FloatField(blank=True, null=True)
    humidity_percents = models.FloatField(blank=True, null=True)
    iron_mg = models.FloatField(blank=True, null=True)
    isoleucine_g = models.FloatField(blank=True, null=True)
    leucine_g = models.FloatField(blank=True, null=True)
    lipidius_g = models.FloatField(blank=True, null=True)
    lysine_g = models.FloatField(blank=True, null=True)
    magnesium_mg = models.FloatField(blank=True, null=True)
    manganese_mg = models.FloatField(blank=True, null=True)
    methionine_g = models.FloatField(blank=True, null=True)
    monounsaturated_g = models.FloatField(blank=True, null=True)
    niacin_mg = models.FloatField(blank=True, null=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    phenylalanine_g = models.FloatField(blank=True, null=True)
    phosphorus_mg = models.FloatField(blank=True, null=True)
    polyunsaturated_g = models.FloatField(blank=True, null=True)
    potassium_mg = models.FloatField(blank=True, null=True)
    proline_g = models.FloatField(blank=True, null=True)
    protein_g = models.FloatField(blank=True, null=True)
    pyridoxine_mg = models.FloatField(blank=True, null=True)
    rae_mcg = models.FloatField(blank=True, null=True)
    re_mcg = models.FloatField(blank=True, null=True)
    retinol_mcg = models.FloatField(blank=True, null=True)
    riboflavin_mg = models.FloatField(blank=True, null=True)
    saturated_g = models.FloatField(blank=True, null=True)
    serine_g = models.FloatField(blank=True, null=True)
    sodium_mg = models.FloatField(blank=True, null=True)
    threonine_g = models.FloatField(blank=True, null=True)
    tiamina_mg = models.FloatField(blank=True, null=True)
    tryptophan_g = models.FloatField(blank=True, null=True)
    tyrosine_g = models.FloatField(blank=True, null=True)
    valine_g = models.FloatField(blank=True, null=True)
    vitaminc_mg = models.FloatField(blank=True, null=True)
    zinc_mg = models.FloatField(blank=True, null=True)



    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'alimento'
