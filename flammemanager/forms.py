from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['id_commande','client','produits','prix_ttc','commande']
