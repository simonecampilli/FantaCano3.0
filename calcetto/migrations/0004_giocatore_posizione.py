# Generated by Django 4.1.7 on 2023-04-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcetto', '0003_giocatore_immagine'),
    ]

    operations = [
        migrations.AddField(
            model_name='giocatore',
            name='posizione',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
