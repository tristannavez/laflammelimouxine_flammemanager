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
    list_filter = ('etat_commande', 'produits')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")

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
    list_display = ('__str__', 'client', 'etat_livraison', 'commande', 'date_reelle')
    list_filter = (LivraisonEtatListFilter,'client', 'date_reelle')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")


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
    list_display = ('__str__', 'client', 'etat_chantier', 'nombre_de_jours', 'date_intervention', 'type_chantier')
    list_filter = (ChantierEtatListFilter, 'nombre_de_jours', 'date_intervention', 'type_chantier')
    search_fields = ('client__nom',)
    search_help_text = ("Rechercher un client")
    exclude = ('livraisons',)
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