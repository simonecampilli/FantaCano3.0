from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Giocatore(models.Model):

    nome = models.CharField(max_length=50)
    soprannome = models.CharField(max_length=50)
    punti_totalizzati = models.IntegerField(default=0)
    partite_giocate = models.IntegerField(default=0)
    gol = models.IntegerField(default=0)
    assist = models.IntegerField(default=0)
    fanta_media = models.FloatField(default=6.0)
    immagine = models.ImageField(null= True, blank= True, upload_to = "images/")
    posizione = models.CharField(max_length=100, blank=True, null=True)
    immagine2=models.ImageField(null= True, blank= True, upload_to = "images/")
    def __str__(self):
        return self.nome + " (" + self.soprannome + ")"

class Profilo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    giocatore_associato = models.ForeignKey(Giocatore, on_delete=models.CASCADE, null=True, blank=True)
from django import forms
class Partita(models.Model):
    data = models.DateField()
    punteggio_squadra_a = models.IntegerField(default=0)
    punteggio_squadra_b = models.IntegerField(default=0)
    squadra_a = models.ManyToManyField('Giocatore', related_name='partite_squadra_a', blank=True)
    squadra_b = models.ManyToManyField('Giocatore', related_name='partite_squadra_b', blank=True)
    partecipazioni = models.ManyToManyField('Giocatore', through='Partecipazione', blank=True)

    def __str__(self):
        return str(self.data) + " - "




class Partecipazione(models.Model):
    giocatore = models.ForeignKey('Giocatore', on_delete=models.CASCADE)
    partita = models.ForeignKey(Partita, on_delete=models.CASCADE)
    gol = models.IntegerField()
    assist = models.IntegerField()

    def __str__(self):
        return str(self.giocatore) + " - " + str(self.partita)

    def save(self, *args, **kwargs):
        # chiamare il metodo save del modello padre per salvare l'oggetto Partecipazione
        super(Partecipazione, self).save(*args, **kwargs)

        # aggiornare le statistiche globali del giocatore
        self.giocatore.gol += self.gol
        self.giocatore.assist += self.assist
        self.giocatore.partite_giocate += 1

        # aggiornare la squadra del giocatore nella partita
        if self.giocatore in self.partita.squadra_a.all():
            self.partita.squadra_a.add(self.giocatore)
            self.partita.squadra_b.remove(self.giocatore)
            self.partita.punteggio_squadra_a+= self.gol

        elif self.giocatore in self.partita.squadra_b.all():
            self.partita.squadra_b.add(self.giocatore)
            self.partita.squadra_a.remove(self.giocatore)
            self.partita.punteggio_squadra_b += self.gol

        self.partita.save()
        self.giocatore.save()

