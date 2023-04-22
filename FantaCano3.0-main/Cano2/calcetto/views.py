from django.shortcuts import render

from django.shortcuts import render
from .models import Giocatore

def lista_giocatori(request):
    # Queryset ordinato per punti totalizzati
    giocatori = Giocatore.objects.order_by('-punti_totalizzati')
    context = {'giocatori': giocatori}
    return render(request, 'lista_giocatori.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Partita

def lista_partite(request):
    partite = Partita.objects.all()
    context = {'partite': partite}
    return render(request, 'lista.html', context)



from django.shortcuts import render, get_object_or_404
from .models import Partita, Partecipazione

def dettaglio_partita(request, partita_id):
    partita = get_object_or_404(Partita, pk=partita_id)
    squadra_a = partita.squadra_a.all()
    squadra_b = partita.squadra_b.all()
    partecipazioni = partita.partecipazioni.all()
    partecipazioni2= Partecipazione.objects.all()
    context = {
        'partita': partita,
        'squadra_a': squadra_a,
        'squadra_b': squadra_b,
        'partecipazioni': partecipazioni,
        'partecipazioni2': partecipazioni2,
    }
    return render(request, 'dettaglio.html', context)


from django.shortcuts import render
from calcetto.models import Partecipazione

def visualizza_partecipazioni(request):
    partecipazioni = Partecipazione.objects.all()
    return render(request, 'visualizza_partecipazioni.html', {'partecipazioni': partecipazioni})
