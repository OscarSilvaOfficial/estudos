# Generated by Django 3.0.8 on 2020-07-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('arquivo', models.FileField(upload_to='media/%d-%m-%Y/')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Data de Publicação')),
            ],
            options={
                'verbose_name_plural': 'Lista',
            },
        ),
    ]
