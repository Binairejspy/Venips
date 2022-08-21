

from http import client

from django.shortcuts import render,redirect
from acceuil.models import *
from connexion.forms import Inscription_Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout


# Create your views here.
def connexion(request):
    if request.method=="POST":
      
        nomuser_conec=request.POST['username']
        mot_pass_conec=request.POST['password']
        user=authenticate(username=nomuser_conec,password=mot_pass_conec)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            if nomuser_conec not in Clients.objects.all():
                error_nomutilisateur="Nom d'utilisateur"
                print(error_nomutilisateur)
            if mot_pass_conec not in Clients.objects.all():
                error_motpasse = " mot de passe incorrect"
                print(error_motpasse)
            return render(request,'connexion.html',{'erruser':error_nomutilisateur,'errpass':error_motpasse})


           
    return render(request,'connexion.html')



def inscription(request):
    if request.method=="POST":
        form = Inscription_Form(request.POST, request.FILES)
        try:


            if form.is_valid:
                nom_donne=request.POST['nomclient']
                prenom_donne=request.POST['prenomclient']
                email_donne=request.POST['nomclient']
                nomutilisateur_donne=request.POST['nomutilisateur']
                motdepasse_donne=request.POST['motdepasse']
                motdepasse_conf_donne=request.POST['motdepasse_conf']
          
                numero_donne=request.POST['numero']
                
          
                if motdepasse_donne==motdepasse_conf_donne and len(motdepasse_donne)>=6 and nomutilisateur_donne not in User.objects.all():
                    form.save()
                    create_client=User.objects.create_user(username=nomutilisateur_donne,password=motdepasse_donne)

                    print('le mot de passe est bon  et nom user existe')
                    return redirect('connexion')
                
                else:
                    error_pass = "les mots de passe sont pas conforme ou la taille n'est pas 6 cararacteres"
                    print('mot de passe non correcte ou nomuser existe')
                    
                    return render(request,'inscription.html',{'form':form,'error_pass':error_pass})

            else:
                form = Inscription_Form()
                print('ya des erreurs de validation')
        except:
           pass
    else : 
        form = Inscription_Form()
        print('cest un post ')

    return render(request,'inscription.html',{'form':form})





def deconnexion(request):
     logout(request)
     return redirect('index')



def menu(request):
    client = Clients.objects.all()
    return render(request,'menu.html',{'client':client})

  