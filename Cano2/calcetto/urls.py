from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_giocatori, name='lista_giocatori'),
    path('lista_partite', views.lista_partite, name='lista_partite'),
    path('<int:partita_id>/', views.dettaglio_partita, name='dettaglio_partita'),
]

