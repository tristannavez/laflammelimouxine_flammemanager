from django.db.models.signals import post_save
from .models import Commande, Livraison, Chantier, Solde, PropositionCommerciale
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(post_save, sender=Commande)
def create_livraison_on_commande(sender, instance, **kwargs):
    if instance.etat_commande == 'terminé' and not Livraison.objects.filter(commande=instance).exists():
        new_livraison = Livraison.objects.create(
            client=instance.client,
            commande=instance
        )
        new_livraison.etat_livraison='commandé'
        new_livraison.save()

@receiver(post_save, sender=Livraison)
def create_chantier_on_livraison(sender, instance, **kwargs):
    if instance.etat_livraison == 'complet':
        livraisons_client = Livraison.objects.filter(commande__client=instance.commande.client)
        commandes_en_attente = Commande.objects.filter(client=instance.commande.client, etat_commande='en attente')
        if not commandes_en_attente and all([livraison.etat_livraison == 'complet' for livraison in livraisons_client]):
            new_chantier = Chantier.objects.create(
                client=instance.commande.client,
                etat_chantier='en attente'
            )
            new_chantier.livraisons.set(livraisons_client)



@receiver(post_save, sender=Chantier)
def create_solde_on_chantier(sender, instance, **kwargs):
    if instance.etat_chantier == "terminé" and instance.type_chantier != "intervention légère":
        commande = Commande.objects.filter(client=instance.client).last()
        Solde.objects.create(chantier=instance, client=instance.client, commande=commande, etat_solde="en attente", id_facture=None)


@receiver(pre_save, sender=PropositionCommerciale)
def update_date_entree(sender, instance, **kwargs):
    instance.date_entree = now().date()