# Generated by Django 3.0.8 on 2020-09-06 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmb', '0006_auto_20200906_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tmb',
            name='altura',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='idade',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='peso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tmb',
            name='total',
            field=models.IntegerField(),
        ),
    ]
