
from django.urls import path
from .views import *

urlpatterns = [
    path('allcommande/',lescommendes,name='allcommande'),
    path('traiter/<int:id>',traiter,name='traiter'),
]
