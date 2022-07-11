# Generated by Django 4.0.4 on 2022-06-13 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0005_adres_stadion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('godzina_rozpoczecia', models.DateField()),
                ('wynik', models.CharField(max_length=6)),
                ('gosc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klub2', to='league.klub')),
                ('gospodarz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klub1', to='league.klub')),
                ('sedzia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league.sedzia')),
            ],
        ),
    ]
