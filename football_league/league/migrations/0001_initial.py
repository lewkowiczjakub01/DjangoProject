# Generated by Django 4.0.4 on 2022-06-13 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('wlasciciel', models.CharField(max_length=50)),
                ('data_zalozenia', models.DateField()),
                ('menadzer', models.CharField(max_length=50)),
            ],
        ),
    ]
