# Generated by Django 2.2.7 on 2019-11-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cos', '0003_auto_20191117_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
    ]
