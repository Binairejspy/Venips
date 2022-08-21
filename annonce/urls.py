from django.urls import path
from .views import *
from acceuil.views import *
from boutique.views import *
from annonce.views import *
from connexion.views import *



urlpatterns = [
    path('annonce/',annonce,name='annonce'),
    
    path('<str:element_annonce>',menu_annonces,name='filter_annonce'),
    path('details_annonce/<int:id>',details_annonce,name='details_annonce'),
    path('recherche_annonce/',recherche_annonce,name='recherche_annonce'),
    path('ajout_annonce/',ajout_annonce,name='ajout_annonce'),
    path('contactvendeur/<str:proprietaire>',Contact_vendeur,name='contactvendeur')
    
    
]
