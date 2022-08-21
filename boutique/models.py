from django.db import models
from django.utils import timezone

from acceuil.models import Clients

# Create your models here.
# model pour les articles

class Article(models.Model):

    designation = models.CharField(max_length=45)
    description = models.TextField()
    img = models.ImageField(upload_to='media')
    prix = models.PositiveIntegerField()
    quantité = models.IntegerField()
    Type = models.CharField(max_length=65,default='article')
    

    
    def __str__(self):
        return self.designation


class commandes(models.Model):
    nomusercommande = models.ForeignKey(Clients, verbose_name=("le commandeur"), on_delete=models.CASCADE)
    nomproduitcommande=models.ForeignKey(Article, verbose_name=("le produit commander"), on_delete=models.CASCADE)

class commandes_alls(models.Model):
    nomusercommande_all = models.ForeignKey(Clients, on_delete=models.CASCADE)
    id_produit = models.IntegerField()
    date_commande = models.DateField(default=timezone.now)
    qt = models.IntegerField(default=1)

