# Generated by Django 2.2 on 2020-07-30 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_page', '0003_auto_20200730_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layoutmenssagecontact',
            old_name='address_contact_url',
            new_name='address_contact_text',
        ),
    ]
