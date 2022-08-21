from django.urls import path

from connexion.views import connexion, deconnexion, inscription

urlpatterns = [
    path('connexion/',connexion,name='connexion'),
    path('inscription/',inscription,name='inscription'),
    path('deconnexion/',deconnexion,name='deconnexion')
  
]
