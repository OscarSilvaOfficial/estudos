# Generated by Django 3.0.8 on 2020-07-18 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('ramal', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ramais.Setor')),
            ],
            options={
                'verbose_name_plural': 'Telefones',
            },
        ),
    ]