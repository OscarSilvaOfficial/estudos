# Generated by Django 2.2 on 2020-07-22 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipamento', models.CharField(max_length=50, verbose_name='Equipametos')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
            ],
            options={
                'verbose_name_plural': 'Estoque de TI',
            },
        ),
    ]
