# Generated by Django 3.0.8 on 2020-09-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmb', '0005_auto_20200906_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmb',
            name='altura',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='idade',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='peso',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='total',
            field=models.FloatField(),
        ),
    ]
