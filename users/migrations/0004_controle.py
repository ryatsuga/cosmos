# Generated by Django 2.2.7 on 2019-11-17 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0005_delete_empresaselecionada'),
        ('users', '0003_auto_20191028_2049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plano', models.CharField(choices=[(0, 'Gratuito'), (1, 'Premium')], default=0, max_length=1, verbose_name='Plano')),
                ('limite_empresas', models.IntegerField(default=1, verbose_name='Limite empresas')),
                ('limite_colaboradores', models.IntegerField(default=5, verbose_name='Limite colaboradores')),
                ('empresa_selecionada', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa', verbose_name='Empresa selecionada')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
