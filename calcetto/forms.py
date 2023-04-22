from django import forms
from .models import Partita, Partecipazione, Giocatore

class PartecipazioneForm(forms.ModelForm):
    class Meta:
        model = Partecipazione
        fields = ['giocatore', 'gol', 'assist']
from django import forms

class PartitaForm(forms.ModelForm):
    partecipazioni = forms.inlineformset_factory(
        Partita,
        Partecipazione,
        form=PartecipazioneForm,
        extra=11
    )

    class Meta:
        model = Partita
        fields = ['data', 'punteggio_squadra_a', 'punteggio_squadra_b', 'squadra_a', 'squadra_b']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'squadra_a': forms.CheckboxSelectMultiple,
            'squadra_b': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['squadra_a'].queryset = Giocatore.objects.all()
        self.fields['squadra_b'].queryset = Giocatore.objects.all()