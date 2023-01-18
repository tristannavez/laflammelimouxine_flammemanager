from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client','produits','prix_vente_ht','prix_achat_ht']
