from django.urls import path
from . import views
from .views import visualizza_partecipazioni

urlpatterns = [
    path('', views.lista_giocatori, name='lista_giocatori'),
    path('lista_partite', views.lista_partite, name='lista_partite'),
    path('<int:partita_id>/', views.dettaglio_partita, name='dettaglio_partita'),
path('partecipazioni/', visualizza_partecipazioni, name='partecipazioni'),
]

