from django.contrib import admin
from .models import Giocatore, Partita, Partecipazione
# Register your models here.
admin.site.register(Giocatore)
admin.site.register(Partita)
admin.site.register(Partecipazione)