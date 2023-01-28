from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from .models import Commande, Client, Produit, Livraison, Chantier, Solde

admin_site = AdminSite(name='Mon Administration')
admin_site.site_header = 'Flamme Manager'
admin_site.site_title = 'Flamme Manager'
admin_site.index_title = 'Bienvenue dans Flamme Manager'




# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'adresse', 'email', 'telephone')

class CommandeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'prix_achat_ht', 'prix_vente_ht', 'etat_commande', 'num_devis', 'date_entree', 'commentaire')
    list_filter = ('etat_commande', 'produits', 'date_entree')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")
    exclude = ('date_entree',)

class LivraisonEtatListFilter(admin.SimpleListFilter):
    title = 'Etat de la livraison'
    parameter_name = 'état'

    def lookups(self, request, model_admin):
        return (
            ('commandé_ou_livré', 'Commandé ou Livré'),
            ('commandé', 'Commandé'),
            ('livré', 'Livré'),
            ('complet', 'Complet'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'commandé_ou_livré':
            return queryset.filter(etat_livraison__in=['commandé', 'livré'])
        if self.value() == 'commandé':
            return queryset.filter(etat_livraison__in=['commandé'])
        if self.value() == 'livré':
            return queryset.filter(etat_livraison__in=['livré'])
        if self.value() == 'complet':
            return queryset.filter(etat_livraison__in=['complet'])


class LivraisonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'etat_livraison', 'commande', 'date_commande', 'commentaire')
    list_filter = (LivraisonEtatListFilter, 'date_commande', 'commande__produits')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")
    exclude = ('commande',)


class ChantierEtatListFilter(admin.SimpleListFilter):
    title = 'Etat du chantier'
    parameter_name = 'état'

    def lookups(self, request, model_admin):
        return (
            ('en attente, planifié ou validé', 'En attente, planifié ou validé'),
            ('en attente', 'En attente'),
            ('planifié', 'Planifié'),
            ('validé', 'Validé'),
            ('terminé', 'Terminé'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'en attente, planifié ou validé':
            return queryset.filter(etat_chantier__in=['en attente', 'planifié', 'validé'])
        if self.value() == 'en attente':
            return queryset.filter(etat_chantier__in=['en attente'])
        if self.value() == 'planifié':
            return queryset.filter(etat_chantier__in=['planifié'])
        if self.value() == 'validé':
            return queryset.filter(etat_chantier__in=['validé'])
        if self.value() == 'terminé':
            return queryset.filter(etat_chantier__in=['validé'])

class ChantierAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'client', 'etat_chantier', 'nombre_de_jours', 'date_intervention', 'type_chantier', 'commentaire', 'chantier_commencé')
    list_filter = (ChantierEtatListFilter, 'nombre_de_jours', 'date_intervention', 'type_chantier', 'chantier_commencé')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")
    exclude = ('livraisons',)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fournisseur')
    list_filter = ('nom', 'fournisseur')



class SoldeEtatListFilter(admin.SimpleListFilter):
    title = 'Etat du solde'
    parameter_name = 'état'

    def lookups(self, request, model_admin):
        return (
            ('en_attente_partiel', 'En attente ou partiel'),
            ('en_attente', 'En attente'),
            ('partiel', 'Partiel'),
            ('soldé', 'Soldé'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'en_attente_partiel':
            return queryset.filter(etat_solde__in=['en attente', 'partiel'])
        if self.value() == 'en_attente':
            return queryset.filter(etat_solde__in=['en attente'])
        if self.value() == 'partiel':
            return queryset.filter(etat_solde__in=['partiel'])
        if self.value() == 'soldé':
            return queryset.filter(etat_solde__in=['soldé'])



class SoldeAdmin(admin.ModelAdmin):
    list_display = ('__str__','chantier', 'client', 'etat_solde', 'id_facture', 'num_devis','prix_facture_ht','date_solde')
    list_filter = (SoldeEtatListFilter,'etat_solde','date_solde')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")
    exclude = ('commande',)





admin_site.register(Client, ClientAdmin)
admin_site.register(Commande, CommandeAdmin)
admin_site.register(Livraison, LivraisonAdmin)
admin_site.register(Chantier, ChantierAdmin)
admin_site.register(Produit, ProduitAdmin)
admin_site.register(Solde, SoldeAdmin)
admin_site.register(User)
admin_site.register(Group)