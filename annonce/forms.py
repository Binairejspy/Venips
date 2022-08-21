
from django import forms

from .models import Annonces

class Annonces_Form(forms.ModelForm):
    
    class Meta:
        model = Annonces
        fields = ('__all__')
        exclude = ('vendeur','numero_vendeur','email_vendeur')
    
        widgets = {
            'desi_annonce':forms.TextInput(attrs={'class':'form-control '}),
            'prix_annonce':forms.TextInput(attrs={'class':'form-control '}),
            'img_annonce':forms.FileInput(attrs={'class':'form-control '}),
            'lieu_produit':forms.TextInput(attrs={'class':'form-control'}),
            'nature':forms.Select(attrs={'class':'form-control '}),
            'A_type':forms.Select(attrs={'class':'form-control '}),
            'desc_annonce':forms.TextInput(attrs={'class':'form-control '}),
           






        }

    
  