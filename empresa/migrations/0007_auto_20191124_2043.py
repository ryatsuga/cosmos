# Generated by Django 2.2.7 on 2019-11-24 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_colaborador_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='identificacao',
            field=models.CharField(max_length=14, verbose_name='CPF/CNPJ'),
        ),
    ]
