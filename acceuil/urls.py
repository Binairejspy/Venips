
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('index',index,name='index'),
    path('apropos',apropos,name='apropos'),
    path('contact',contact,name='contact'),
    path('help',help,name='help'),
    
]
