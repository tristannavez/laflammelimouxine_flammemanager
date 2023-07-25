from django.db import models
from datetime import date
from django.contrib import admin


class Client(models.Model):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)


    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    fournisseur = models.CharField(max_length=200)

    def __str__(self):
        return self.nom

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produits = models.ManyToManyField(Produit)
    prix_achat_ht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix_vente_ht = models.DecimalField(max_digits=10, decimal_places=2)
    etat_commande = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('terminé', 'Terminé')])
    date_entree = models.DateField(default=date.today)
    num_devis = models.CharField(max_length=20)
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return 'Commande pour '+str(self.client)+' contenant : '+str([str(p) for p in self.produits.all()])

class Livraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    etat_livraison = models.CharField(max_length=20, choices=[('commandé', 'Commandé'), ('livré', 'Livré'), ('complet', 'Complet')])
    date_commande = models.DateField(default=date.today)
    def __str__(self):
        return 'Livraison pour ' + str(self.commande.client) + ' contenant : ' + str([str(p) for p in self.commande.produits.all()])

    def num_devis(self):
        return self.commande.num_devis
    def commentaire(self):
        return self.commande.commentaire
class Chantier(models.Model):
    livraisons = models.ManyToManyField(Livraison)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_chantier = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('planifié', 'Planifié'), ('validé', 'Validé'), ('terminé', 'Terminé')])
    nombre_de_jours = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    date_intervention = models.DateField(default=date.today, null=True, blank=True)
    type_chantier = models.CharField(max_length=22, choices=[('intervention légère', 'Intervention légère'), ('intervention classique', 'Intervention classique')])
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    chantier_commencé = models.BooleanField(default=False)
    def __str__(self):
        return 'Chantier pour ' + str(self.client.nom)

    def num_devis(self):
        livraison = self.livraisons.first()  # prendre la première livraison associée au chantier
        if livraison:
            return livraison.commande.num_devis
        return ''

class Solde(models.Model):
    chantier = models.ForeignKey(Chantier, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    etat_solde = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('partiel', 'Partiel'), ('soldé', 'Soldé')])
    id_facture = models.CharField(max_length=20, null=True, blank=True)
    prix_facture_ht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_solde = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Solde pour : ' + str(self.chantier)
    def num_devis(self):
        if self.commande is not None:
            return self.commande.num_devis
        return None

class PropositionCommerciale(models.Model):
    STATUT_CHOICES = [
        ('envoye', 'Envoyé'),
        ('rappel', 'Rappelé'),
        ('attente', 'En attente'),
        ('auaide', 'Au aide'),
        ('valide', 'Validé'),
        ('perdu', 'Perdu'),
    ]

    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    date_devis = models.DateField(default=date.today)
    numero_devis = models.CharField(max_length=20)
    type_devis = models.CharField(max_length=100)
    marque = models.CharField(max_length=100)
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    commentaire = models.TextField(blank=True, null=True)
    date_entree = models.DateField(default=date.today)
    def __str__(self):
        return f"Proposition {self.numero_devis} - {self.client}"

class Echeancier(models.Model):

    STATUT_CHOICES = [
        ('virement', 'Virement'),
        ('prelevement', 'Prélèvement'),
        ('cheque', 'Chèque'),
        ('especes', 'Espèces'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_facture = models.DateField()
    date_echeance = models.DateField()
    type_paiement = models.CharField(max_length=20, choices=STATUT_CHOICES)
    montant_total_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    statut = models.CharField(max_length=20, choices=[
        ('en attente', 'En attente'),
        ('partiellement payé', 'Partiellement payé'),
        ('payé', 'Payé'),
        ('en retard', 'En retard'),
        ('annulé', 'Annulé')
    ])
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"Échéancier pour le client {self.client.nom}"

from . import signals
