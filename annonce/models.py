
from django.db import models
from django.db.models.deletion import CASCADE
from acceuil.models import Clients

# Create your models here.

# model pour les annonces

class Annonces(models.Model):

    choix_type_annonce = [
        ('vetement','vetement'),
        ('chaussure','chaussure'),
        ('chemise','chemise'),
        ('technologie','technologie'),
        ('telephone','telephone'),
        ('ordinateur','ordinateur'),
        ('autre','autre')
    ]


    choix_nature = [
        ('occasion','occasion'),
        ('nouveau','nouveau')
    ]

    desi_annonce = models.CharField(max_length=25,verbose_name="designation d'annonce")    
    prix_annonce = models.PositiveIntegerField()
    img_annonce = models.ImageField(upload_to='media/annonces',default='img',verbose_name="image d'annonce")
    vendeur =models.ForeignKey(Clients,on_delete=CASCADE)
    
    lieu_produit = models.CharField(max_length=45,default='conakry')
    
    nature = models.CharField(max_length=50,default='occasion',choices=choix_nature)
    A_type= models.CharField( max_length=50,default='autre',choices=choix_type_annonce)
    desc_annonce = models.TextField(default='pas de description',verbose_name="description de l'annonce")


    def __str__(self):
        return self.desi_annonce


