# Generated by Django 2.2 on 2020-07-30 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_page', '0005_auto_20200730_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutMenssageContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data da adição')),
                ('email_contact_text', models.EmailField(max_length=254, verbose_name='Texto de contato para E-mail')),
                ('address_contact_text', models.TextField(verbose_name='Texto de contato para Endereço')),
                ('phone_contact_text', models.TextField(verbose_name='Texto de contato para telefone')),
            ],
            options={
                'verbose_name_plural': 'Mensagem do Layout de Contato',
            },
        ),
        migrations.CreateModel(
            name='LayoutMenssagePresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now=True, verbose_name='Data da adição')),
                ('presentation_text', models.TextField(verbose_name='Texto de Apresentação da Aplicação')),
            ],
            options={
                'verbose_name_plural': 'Mensagem do Layout de Apresentação',
            },
        ),
        migrations.DeleteModel(
            name='LayoutMenssage',
        ),
        migrations.AddField(
            model_name='layoutmenssagecontact',
            name='pk_layout_presentation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_home_page.LayoutMenssagePresentation', verbose_name='Menssagem do Layout de Apresentação'),
        ),
    ]