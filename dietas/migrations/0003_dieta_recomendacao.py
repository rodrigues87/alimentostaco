# Generated by Django 3.0.8 on 2020-07-20 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recomendado', '0001_initial'),
        ('dietas', '0002_dieta_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='dieta',
            name='recomendacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recomendado.Recomendado'),
        ),
    ]