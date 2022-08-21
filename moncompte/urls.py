from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
path('profile/',moncompte,name="moncompte"),
path('supp/<int:id>',supprimer,name='supp'),
path('modif/<int:id>',modifier,name='modif'),
path('changer_photo/',changer_photo,name='changer_photo')
    
]
