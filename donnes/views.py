from django.shortcuts import redirect, render

from boutique.migrations import *
from django.contrib.auth.decorators import permission_required
from boutique.models import *
from boutique.views import all_commande

# Create your views here.
@permission_required('boutique.commandes_alls')
def lescommendes(request):
    allcommande=commandes_alls.objects.all()
    try:
        if request.method=='POST':
            id_string = request.POST['id_produit']
            id_int = int(id_string)
            
        
            correspondant = Article.objects.get(id=id_int)
        
            return render(request,'allcommande.html',{'allcmmd':allcommande,'img_produit':correspondant,
                                                   })
        
    except:

        return render(request,'allcommande.html',{'allcmmd':allcommande})



    return render(request,'allcommande.html',{'allcmmd':allcommande})

@permission_required('boutique.commandes_alls')
def traiter(request,id):
    commandes_alls.objects.get(id=id).delete()
  
    return redirect('allcommande')