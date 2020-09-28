# Generated by Django 3.0.8 on 2020-07-18 04:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('valor_unitario', models.DecimalField(blank=True, decimal_places=2, max_digits=15, verbose_name='Valor Unitário em R$')),
                ('usuario', models.ManyToManyField(default=1, to=settings.AUTH_USER_MODEL, verbose_name='Seleção de Usuário')),
            ],
            options={
                'verbose_name_plural': 'Licenças',
            },
        ),
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenca', models.ManyToManyField(to='app_licencas.Licenca')),
            ],
            options={
                'verbose_name_plural': 'Custos Totais',
            },
        ),
    ]