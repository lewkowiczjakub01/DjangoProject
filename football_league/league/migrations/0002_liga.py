# Generated by Django 4.0.4 on 2022-06-13 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('ilosc_klubow', models.IntegerField(max_length=30)),
                ('ilosc_punktow', models.IntegerField(max_length=30)),
                ('bilans_bramkowy', models.IntegerField(max_length=30)),
                ('kluby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.klub')),
            ],
        ),
    ]