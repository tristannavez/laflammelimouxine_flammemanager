from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Commande, Client, Produit, Livraison, Chantier

admin_site = AdminSite(name='Mon Administration')
admin_site.site_header = 'Flamme Manager'
admin_site.site_title = 'Flamme Manager'
admin_site.index_title = 'Bienvenue dans Flamme Manager'




# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'adresse', 'email', 'telephone', 'num_devis')

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'prix_achat_ht', 'prix_vente_ht', 'etat_commande')
    list_filter = ('client', 'etat_commande')

class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'etat_livraison', 'commande', 'date_reelle')
    list_filter = ('client', 'etat_livraison', 'date_reelle')


class ChantierAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'etat_chantier', 'nombre_de_jours', 'date_intervention', 'type_chantier')
    list_filter = ('etat_chantier', 'client', 'nombre_de_jours', 'date_intervention', 'type_chantier')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fournisseur')
    list_filter = ('nom', 'fournisseur')


admin_site.register(Client, ClientAdmin)
admin_site.register(Commande, CommandeAdmin)
admin_site.register(Livraison, LivraisonAdmin)
admin_site.register(Chantier, ChantierAdmin)
admin_site.register(Produit, ProduitAdmin)
admin_site.register(User)
admin_site.register(Group)