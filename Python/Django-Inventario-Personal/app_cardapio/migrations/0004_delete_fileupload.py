# Generated by Django 2.2 on 2020-08-01 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cardapio', '0003_auto_20200801_1831'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileUpload',
        ),
    ]