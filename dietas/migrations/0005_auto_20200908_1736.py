# Generated by Django 3.0.8 on 2020-09-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0004_dieta_tmb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieta',
            name='total_alanine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_arginine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_ashes_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_aspartic_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_calcium_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_carbohydrate_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_cholesterol_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_copper_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_cystine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_energy_kcal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_energy_kj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_fiber_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_glutamic_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_glycine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_histidine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_humidity_percents',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_iron_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_isoleucine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_leucine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_lipidius_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_lysine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_magnesium_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_manganes_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_methionine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_monounsaturated_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_niacin_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_phenylalanine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_phosphorus_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_polyunsaturated_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_potassium_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_proline_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_protein_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_pyridoxine_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_rae_mcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_re_mcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_retinol_mcg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_riboflavin_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_saturated_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_serine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_sodium_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_threonine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_tiamina_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_tryptophan_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_tyrosine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_valine_g',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_vitaminc_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dieta',
            name='total_zinc_mg',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]