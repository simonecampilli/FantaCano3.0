# Generated by Django 4.1.7 on 2023-04-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calcetto', '0007_alter_partita_punteggio_totale'),
    ]

    operations = [
        migrations.AddField(
            model_name='giocatore',
            name='immagine2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
