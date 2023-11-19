import admin_interface.models
from django.contrib import admin
from django.contrib.admin import AdminSite
from admin_interface import *
from django.contrib.auth.models import User, Group
from .models import Commande, Client, Produit, Livraison, Chantier, Solde, PropositionCommerciale, Echeancier

admin_site = AdminSite(name='Mon Administration')
admin_site.site_header = 'Flamme Manager'
admin_site.site_title = 'Flamme Manager'
admin_site.index_title = 'Bienvenue dans Flamme Manager'


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'adresse', 'email', 'telephone')


class CommandeAdmin(admin.ModelAdmin):
    list_display = (
    '__str__', 'client', 'prix_achat_ht', 'prix_vente_ht', 'etat_commande', 'num_devis', 'date_entree', 'commentaire')
    list_filter = ('etat_commande', 'produits', 'date_entree')
    search_fields = ('client__nom', 'client__email', 'client__telephone', 'num_devis')
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
    list_display = ('__str__', 'client', 'etat_livraison', 'date_commande', 'commentaire', 'num_devis')
    list_filter = (LivraisonEtatListFilter, 'commande__produits', 'date_commande')
    search_fields = ('client__nom', 'client__email', 'client__telephone')
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
    list_display = (
    '__str__', 'client', 'etat_chantier', 'nombre_de_jours', 'date_intervention', 'type_chantier', 'commentaire',
    'chantier_commencé', 'num_devis')
    list_filter = (ChantierEtatListFilter, 'nombre_de_jours', 'type_chantier', 'chantier_commencé', 'date_intervention')
    search_fields = ('client__nom', 'client__email', 'client__telephone')
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
    list_display = (
    '__str__', 'chantier', 'client', 'etat_solde', 'id_facture', 'num_devis', 'prix_facture_ht', 'date_solde')
    list_filter = (SoldeEtatListFilter, 'etat_solde', 'date_solde')
    search_fields = ('client__nom', 'client__email', 'client__telephone', 'id_facture', 'num_devis')
    search_help_text = ("Rechercher un client")
    exclude = ('commande',)



class PropositioCommercialeEtatListFilter(admin.SimpleListFilter):
    title = 'Statut proposition'
    parameter_name = 'statut'

    def lookups(self, request, model_admin):
        return (
            ('rappele_en_attente_aux_aides', 'Rappelé en attente ou aux aides'),
            ('envoye', 'Envoyé'),
            ('attente', 'En attente'),
            ('rappel', 'Rappelé'),
            ('auaide', 'Au aide'),
            ('valide', 'Validé'),
            ('perdu', 'Perdu'),

        )

    def queryset(self, request, queryset):
        if self.value() == 'rappele_en_attente_aux_aides':
            return queryset.filter(statut__in=['attente', 'rappel', 'auaide'])
        if self.value() == 'envoye':
            return queryset.filter(statut__in=['envoye'])
        if self.value() == 'attente':
            return queryset.filter(statut__in=['attente'])
        if self.value() == 'rappel':
            return queryset.filter(statut__in=['rappel'])
        if self.value() == 'auaide':
            return queryset.filter(statut__in=['auaide'])
        if self.value() == 'valide':
            return queryset.filter(statut__in=['valide'])
        if self.value() == 'perdu':
            return queryset.filter(statut__in=['perdu'])
class PropositionCommercialeAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_devis', 'numero_devis', 'type_devis', 'montant_ht', 'statut', 'date_entree', 'commentaire')
    list_filter = (PropositioCommercialeEtatListFilter,'date_devis','date_entree')
    search_fields = ('client__nom', 'client__email', 'client__telephone', 'numero_devis')
    search_help_text = ("Rechercher un client")
    exclude = ('date_entree',)

class EcheancierAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_facture', 'date_echeance', 'type_paiement', 'montant_total_ttc', 'montant_paye', 'statut', 'commentaire')
    list_filter = ('client', 'statut', 'date_facture', 'date_echeance', 'type_paiement')
    search_fields = ('client__nom', 'client__email', 'client__telephone')

class AdminTheme(admin.ModelAdmin):
    list_display = ('name','active')

#admin_site.register(Client, ClientAdmin)
#admin_site.register(Commande, CommandeAdmin)
#admin_site.register(Livraison, LivraisonAdmin)
#admin_site.register(Chantier, ChantierAdmin)
#admin_site.register(Produit, ProduitAdmin)
#admin_site.register(Solde, SoldeAdmin)
#admin_site.register(PropositionCommerciale, PropositionCommercialeAdmin)
#admin_site.register(Echeancier, EcheancierAdmin)
#admin_site.register(User)
#admin_site.register(Group)
#admin_site.register(admin_interface.models.Theme, AdminTheme)
