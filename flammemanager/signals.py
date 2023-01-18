from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Commande, Livraison, Chantier

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
        client_livraisons_complet = all([livraison.etat_livraison == 'complet' for livraison in livraisons_client])
        if client_livraisons_complet:
            new_chantier = Chantier.objects.create(
                client=instance.commande.client,
                etat_chantier='en attente'
            )
            new_chantier.livraisons.set(livraisons_client)

