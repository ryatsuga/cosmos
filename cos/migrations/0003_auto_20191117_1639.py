# Generated by Django 2.2.7 on 2019-11-17 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0002_auto_20191111_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordem',
            name='defeito',
            field=models.CharField(max_length=60, null=True, verbose_name='Defeito'),
        ),
        migrations.AddField(
            model_name='ordem',
            name='observacao',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Observações'),
        ),
    ]
