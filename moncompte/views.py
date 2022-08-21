from django.shortcuts import redirect, render
from acceuil.models import *
from annonce.models import *
from django.contrib.auth.decorators import login_required
from boutique.views import nombre
# Create your views here.
@login_required
def moncompte(request):
    user_connect =request.user
      #permet de recuperer  le nombre dans le pannier et le profil utilisateur
    user = request.user
    user_connect = Clients.objects.get(nomutilisateur=user)
    nombre_les_commande_commendeur=nombre(request)
    try:
        info_user = Clients.objects.get(nomutilisateur=user_connect)
        
        annonce_user=Annonces.objects.filter(vendeur_id=info_user.id)
        print(annonce_user)
    except:
        return redirect('connexion')

   
    return render(request,'moncompte.html',{'info':info_user,'annonce_user':annonce_user,'nbr':nombre_les_commande_commendeur,'user_connect':user_connect})

#la modification d'un annonce par son proprietaire
@login_required
def modifier(request,id):
    user = request.user

    info_vendeur = Clients.objects.get(nomutilisateur=user)
    annonce_modif = Annonces.objects.get(id=id)
      #permet de recuperer  le nombre dans le pannier et le profil utilisateur
    user_connect = Clients.objects.get(nomutilisateur=user)
    nombre_les_commande_commendeur=nombre(request)
    if request.method =='POST':
        desig = request.POST['designation']
        prix = request.POST['prix']
        lieu = request.POST['lieu']
        type = request.POST['type']
        img = request.FILES['img']
        nature = request.POST['nature']
        description = request.POST['description']
     
        annonce_modif.desi_annonce=desig
        annonce_modif.prix_annonce = prix
        annonce_modif.lieu_produit = lieu
        annonce_modif.A_type = type
        annonce_modif.nature = nature
        annonce_modif.desc_annonce = description
        annonce_modif.vendeur = info_vendeur
        annonce_modif.img_annonce = img
        
        annonce_modif.save()
        return redirect('moncompte')       
    return render(request,'modifier.html',{'annonce_modif':annonce_modif,'nbr':nombre_les_commande_commendeur,'user_connect':user_connect})

#la suppression d'un annonce 

def supprimer(request,id):
    annonce_supp = Annonces.objects.get(id=id).delete()

    return redirect('moncompte')


def changer_photo(request):
    user = request.user

    info_vendeur = Clients.objects.get(nomutilisateur=user)
    if request.method =='POST':
        img = request.FILES['profile']
        info_vendeur.profil = img
        info_vendeur.save()
        return redirect('moncompte')
        
        