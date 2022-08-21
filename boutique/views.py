
from django.db.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,HttpResponse,redirect
from .models import *

def boutique(request):
    touts = Article.objects.all()
    try:
        user = request.user
        user_connect = Clients.objects.get(nomutilisateur=user)
        nombre_les_commande_commendeur=nombre(request)
        return render(request,'boutique.html',{'ts':touts,'nbr':nombre_les_commande_commendeur,'user_connect':user_connect
                                           })
    except ObjectDoesNotExist:
        print('erreur')

    
    return render(request,'boutique.html',{'ts':touts})
#creation une fonction qui permet de filter les produits
def boutique_filter(request,type):
    touts = Article.objects.filter(Type__icontains=type)
    try :#gestion d'erreur si user n'est pas connecté
            user = request.user
            user_connect = Clients.objects.get(nomutilisateur=user)
            nombre_les_commande_commendeur=nombre(request)
            return render(request,'boutique.html',{'ts':touts,'nbr':nombre_les_commande_commendeur,
                                           'user_connect':user_connect
                                           })

    except :
            pass

    
    return render(request,'boutique.html',{'ts':touts})




def details(request,id):
    pointe = Article.objects.get(id=id)
    #permet de recuperer  le nombre dans le pannier et le profil utilisateur
    type_produit = pointe.Type
    categorie_produit = Article.objects.filter(Type__icontains=type_produit)
    try:#gestion d'erreur si user n'est pas connecté
            user = request.user

            
            user_connect = Clients.objects.get(nomutilisateur=user)
            nombre_les_commande_commendeur=nombre(request)
            return render(request,'details.html',{'pointe':pointe,'nbr':nombre_les_commande_commendeur,'user_connect':user_connect,
                                       'categorie':categorie_produit           })

    except:
            pass
    
    return render(request,'details.html',{'pointe':pointe,'categorie':categorie_produit})



def recherche(request):
    mot = request.GET['mots']
    trouver = Article.objects.filter(designation__icontains=mot)
    try:#gestion d'erreur si user n'est pas connecté
            user = request.user
            user_connect = Clients.objects.get(nomutilisateur=user)
            nombre_les_commande_commendeur=nombre(request)
            return render(request,'recherche.html',{'trouver':trouver,'mot':mot,'nbr':nombre_les_commande_commendeur,'user_connect':user_connect})

    except:
            pass
    return render(request,'recherche.html',{'trouver':trouver,'mot':mot})




def ajout_commande(request):
    if request.method == 'GET':
        commedeur = request.user
        renseignement_commendeur = Clients.objects.get(nomutilisateur = commedeur)
       
        id = request.GET['id_a']
        article_correspondant = Article.objects.get(id=id)
        cmmd = commandes()
        cmmd.nomusercommande = renseignement_commendeur
        cmmd.nomproduitcommande = article_correspondant
        cmmd.save()

        
    return HttpResponse('hello')


def panier(request):
    commendeur = request.user
    renseignement = Clients.objects.get(nomutilisateur = commendeur)
    tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement.id)
    '''calculer la somme total des produits dans le pannier'''
    total = 0
    for i in tout_commande_commendeur:
        total = i.nomproduitcommande.prix + total
    
     #permet de recuperer  le nombre dans le pannier et le profil utilisateur
  
    try:#gestion d'erreur si user n'est pas connecté
            user = request.user
            commendeur = Clients.objects.get(nomutilisateur=commendeur)
            nombre_les_commande_commendeur=nombre(request)
            return render(request,'panier.html',{'tsc':tout_commande_commendeur,'total':total,'nbr':nombre_les_commande_commendeur,'user_connect':commendeur})

    except:
            pass
    
   
    


    return render(request,'panier.html',{'tsc':tout_commande_commendeur,'total':total})


def suppression(request,id):
    commandes.objects.get(id=id).delete()
    return redirect('panier')


def all_commande(request):
    
    user = request.user
    renseignement = Clients.objects.get(nomutilisateur = user)
    tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement.id)
     #permet de recuperer  le nombre dans le pannier et le profil utilisateur
    try:#gestion d'erreur si user n'est pas connecté
            user = request.user
            user_connect = Clients.objects.get(nomutilisateur=user)
            nombre_les_commande_commendeur=nombre(request)
            for i in tout_commande_commendeur:
                    cmmd= commandes_alls()
                    cmmd.nomusercommande_all = renseignement
                    cmmd.id_produit = i.nomproduitcommande_id
                    cmmd.save()
            for i in commandes_alls.objects.all():
                    print(i.nomusercommande_all.nomutilisateur)
                    les_commandes = Article.objects.filter(id = i.id_produit)
                    print(les_commandes)
            tout_commande_commendeur.delete()

            return render(request,'felicitation.html',{'nbr':nombre_les_commande_commendeur,'user_connect':user_connect})
           
   
   
    except:
            pass
    
   
    return render(request,'felicitation.html')

def one_commande(request,id):
    
   #permet de recuperer  le nombre dans le pannier et le profil utilisateur
    try:#gestion d'erreur si user n'est pas connecté
            user = request.user
            user_connect = Clients.objects.get(nomutilisateur=user)
            nombre_les_commande_commendeur=nombre(request)
            
            if request.method =='POST':
                        qt = request.POST['quantité']
                
                        cmmd = commandes_alls()
                        cmmd.nomusercommande_all = user_connect
                        cmmd.id_produit = id
                        cmmd.qt = qt
                        cmmd.save()
            return render(request,'felicitation.html',{'nbr':nombre_les_commande_commendeur,'user_connect':user_connect})
    except:
            pass
    
   
    

    return render(request,'felicitation.html')

#creation  d'une fonction qui permet de recuperer le notre d'element dans le pannier et la photo de profile du client connecté


def nombre(request):
    user = request.user #recuperer user connecter
    '''recuperation des renseignement de user connecter'''

    try: 
        renseignement_commendeur = Clients.objects.get(nomutilisateur = user)
        '''recuperation de commande du client connecter'''
        tout_commande_commendeur= commandes.objects.filter(nomusercommande_id=renseignement_commendeur.id)
        '''recuperation le nombre exacte de ses commandes'''
        return len(tout_commande_commendeur)
    except:
        '''quand ya une exception le nombre est zero'''
        return 0