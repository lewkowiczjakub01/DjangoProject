# Generated by Django 4.0.4 on 2022-06-13 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0006_mecz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klub',
            old_name='menadzer',
            new_name='prezes',
        ),
        migrations.RenameField(
            model_name='klub',
            old_name='wlasciciel',
            new_name='zalozyciel',
        ),
    ]
