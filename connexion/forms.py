
from django import forms
from acceuil.models import Clients

class Inscription_Form(forms.ModelForm):
    
    class Meta:
        model = Clients
        fields = ('__all__')
    
        widgets = {
            'nomclient':forms.TextInput(attrs={'class':'form-control '}),
            'prenomclient':forms.TextInput(attrs={'class':'form-control '}),
            'emailclient':forms.EmailInput(attrs={'class':'form-control '}),
            'profil =':forms.FileInput(attrs={'class':'form-control '}),
            'nomutilisateur':forms.TextInput(attrs={'class':'form-control'}),
            'motdepasse':forms.PasswordInput(attrs={'class':'form-control '}),
            'motdepasse_conf':forms.PasswordInput(attrs={'class':'form-control '}),
            'numero':forms.TextInput(attrs={'class':'form-control '}),
           






        }

    
  