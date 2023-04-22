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



from django.shortcuts import render, redirect
from .models import Partita, Giocatore, Partecipazione
from .forms import PartitaForm, PartecipazioneForm

from django.shortcuts import render, redirect
from .models import Partita, Giocatore, Partecipazione
from .forms import PartitaForm, PartecipazioneForm
'''
def inserisci_partita(request):
    if request.method == 'POST':
        form = PartitaForm(request.POST)
        if form.is_valid():
            partita = form.save(commit=False)
            partita.save()
            return redirect('inserisci_partecipazione', partita_id=partita.id)
    else:
        form = PartitaForm()
    return render(request, 'inserisci_partita.html', {'form': form})
'''
from django.shortcuts import render, redirect
from .models import Partita

def inserisci_partita(request):
    if request.method == 'POST':
        data = request.POST['data']
        punteggio_squadra_a = request.POST['punteggio_squadra_a']
        punteggio_squadra_b = request.POST['punteggio_squadra_b']
        squadra_a = request.POST.getlist('squadra_a')
        squadra_b = request.POST.getlist('squadra_b')

        partita = Partita.objects.create(data=data, punteggio_squadra_a=punteggio_squadra_a, punteggio_squadra_b=punteggio_squadra_b)
        partita.squadra_a.add(*squadra_a)
        partita.squadra_b.add(*squadra_b)
        print(partita.id)
        return redirect(inserisci_partecipazione, partita_id=partita.id)

    giocatori = Giocatore.objects.all()
    context = {'giocatori': giocatori}
    return render(request, 'inserisci_partita.html', context)

def inserisci_partecipazione(request, partita_id):
    partita = Partita.objects.get(id=partita_id)
    if request.method == 'POST':
        form = PartecipazioneForm(request.POST)
        if form.is_valid():
            partecipazione = form.save(commit=False)
            partecipazione.partita = partita
            partecipazione.save()
            return redirect('inserisci_partecipazione', partita_id=partita_id)
    else:
        form = PartecipazioneForm()
    return render(request, 'inserisci_partecipazione.html', {'form': form, 'partita': partita})
