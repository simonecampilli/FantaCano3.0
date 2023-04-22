from django.urls import path
from . import views
from .views import visualizza_partecipazioni, inserisci_partita, inserisci_partecipazione

urlpatterns = [
    path('', views.lista_giocatori, name='lista_giocatori'),
    path('lista_partite', views.lista_partite, name='lista_partite'),
    path('<int:partita_id>/', views.dettaglio_partita, name='dettaglio_partita'),
    path('partecipazioni/', visualizza_partecipazioni, name='partecipazioni'),
    path('inserisci_partita/', inserisci_partita, name='inserisci_partita'),
    path('inserisci_partecipazione/<int:partita_id>/', inserisci_partecipazione, name='inserisci_partecipazione'),
]

