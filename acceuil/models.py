

from importlib.metadata import requires
from django.db import models

# Create your models he

#model client

class Clients (models.Model):

    nomclient=models.CharField(max_length=25,verbose_name='Nom')
    prenomclient=models.CharField(max_length=25,verbose_name='Prenom')
    emailclient=models.EmailField(max_length=45,unique=True,verbose_name='Email',error_messages={'unique':'email existe dejà'})
    nomutilisateur = models.CharField(max_length= 25,unique=True,verbose_name="Nom d'utilisateur",error_messages={'unique':'cet nom utilisateur est dejà pris'})
    motdepasse=models.CharField(max_length=8,verbose_name='mot de passe')
    motdepasse_conf=models.CharField(max_length=8,verbose_name='confirmation mot de passe')
    profil = models.ImageField(upload_to='media/profil',default='media/user.svg',error_messages={'non':'donnez une photo de profile'})
    numero = models.IntegerField(verbose_name='numero telephone')

    def __str__(self):
        return self.nomutilisateur

   
#les tables pour freelance car ya un probleme de  nature inconnu dans le models





class commenteur (models.Model):
     posteur =models.CharField(max_length=255)
     message =models.TextField()
    

   
