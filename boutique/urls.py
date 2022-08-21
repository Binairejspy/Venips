from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import *
from acceuil.views import*
from annonce.views import *
from connexion.views import *
from moncompte.views import moncompte


urlpatterns = [
    
    path('boutique/',boutique,name='boutique'),
    path('boutique_filter/<str:type>',boutique_filter,name='boutique_filter'),




    path('details/<int:id>',details,name='details'),
  

    path('recherche/',recherche,name='recherche'),
    path('ordinateur/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('chemise/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('ordinateur/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('chaussure/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('telephone/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('vetement/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('boutique/ajout_commande/',ajout_commande,name='ajout_commande'),
    path('boutique_filter/ajout_commande/',ajout_commande,name='ajout_commande'),
    
    
    
    
  
    path('panier/',panier,name='panier'),
    path('suppression/<int:id>',suppression,name='suppression'),
    path('felicitation/',all_commande,name='felicitation'),
    path('commendez/<int:id>',one_commande,name='one_commande')
    
    
]
